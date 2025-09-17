import 'dart:io';
import 'package:html/parser.dart' as html_parser;
import 'package:html/dom.dart' as dom;
import '../models/conversation.dart';

class HtmlParserService {
  static Future<List<Category>> parseAllConversations(String basePath) async {
    final categories = <Category>[];

    // Define the categories based on the directory structure
    final categoryNames = [
      'Education and Study',
      'Home and Daily Life',
      'Leisure and Entertainment',
      'Other Professions',
      'Shopping and Finance',
      'Social Interactions',
      'Software Development',
      'Travel and Transportation',
    ];

    for (final categoryName in categoryNames) {
      final categoryPath = '$basePath/$categoryName';
      final categoryDir = Directory(categoryPath);

      if (await categoryDir.exists()) {
        final conversations = <Conversation>[];
        final files = await categoryDir.list().toList();

        for (final file in files) {
          if (file is File && file.path.endsWith('.htm')) {
            final conversation = await parseConversationFile(
              file.path,
              categoryName,
            );
            if (conversation != null) {
              conversations.add(conversation);
            }
          }
        }

        if (conversations.isNotEmpty) {
          categories.add(
            Category(name: categoryName, conversations: conversations),
          );
        }
      }
    }

    return categories;
  }

  static Future<Conversation?> parseConversationFile(
    String filePath,
    String category,
  ) async {
    try {
      final file = File(filePath);
      final content = await file.readAsString();
      final document = html_parser.parse(content);

      // Extract title from h1 element
      final titleElement = document.querySelector('h1');
      final title = titleElement?.text ?? 'Unknown Conversation';

      // Extract conversation exchanges from table rows
      final exchanges = <SpeakerExchange>[];
      final rows = document.querySelectorAll('tbody tr');

      for (final row in rows) {
        final cells = row.querySelectorAll('td');
        if (cells.length >= 2) {
          final speakerElement = cells[0].querySelector('.role');
          final conversationElement = cells[1];

          final speaker = speakerElement?.text ?? '';
          final englishElement = conversationElement.querySelector('.eng');
          final teluguElement = conversationElement.querySelector('.tel');

          final englishText = englishElement?.text ?? '';
          final teluguText = teluguElement?.text ?? '';

          if (speaker.isNotEmpty &&
              (englishText.isNotEmpty || teluguText.isNotEmpty)) {
            exchanges.add(
              SpeakerExchange(
                speaker: speaker,
                englishText: englishText,
                teluguText: teluguText,
              ),
            );
          }
        }
      }

      if (exchanges.isNotEmpty) {
        return Conversation(
          title: title,
          category: category,
          exchanges: exchanges,
          filePath: filePath,
        );
      }
    } catch (e) {
      print('Error parsing file $filePath: $e');
    }

    return null;
  }

  static String getCategoryDisplayName(String categoryName) {
    // Convert directory names to more readable display names
    final displayNames = {
      'Education and Study': 'Education & Study',
      'Home and Daily Life': 'Home & Daily Life',
      'Leisure and Entertainment': 'Leisure & Entertainment',
      'Other Professions': 'Other Professions',
      'Shopping and Finance': 'Shopping & Finance',
      'Social Interactions': 'Social Interactions',
      'Software Development': 'Software Development',
      'Travel and Transportation': 'Travel & Transportation',
    };

    return displayNames[categoryName] ?? categoryName;
  }
}
