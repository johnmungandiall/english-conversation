import 'package:flutter/foundation.dart' hide Category;
import '../models/conversation.dart';
import '../services/html_parser.dart';
import '../services/preferences_service.dart';

class ConversationProvider with ChangeNotifier {
  List<Category> _categories = [];
  bool _isLoading = false;
  String? _error;

  List<Category> get categories => _categories;
  bool get isLoading => _isLoading;
  String? get error => _error;

  Future<void> loadConversations(String basePath) async {
    _isLoading = true;
    _error = null;
    notifyListeners();

    try {
      _categories = await HtmlParserService.parseAllConversations(basePath);
      _isLoading = false;
      notifyListeners();
    } catch (e) {
      _error = 'Failed to load conversations: $e';
      _isLoading = false;
      notifyListeners();
    }
  }

  List<Conversation> getAllConversations() {
    return _categories.expand((category) => category.conversations).toList();
  }

  List<Conversation> searchConversations(String query) {
    if (query.isEmpty) return getAllConversations();

    final allConversations = getAllConversations();
    return allConversations.where((conversation) {
      final titleMatch = conversation.title.toLowerCase().contains(
        query.toLowerCase(),
      );
      final categoryMatch = conversation.category.toLowerCase().contains(
        query.toLowerCase(),
      );
      final contentMatch = conversation.exchanges.any(
        (exchange) =>
            exchange.englishText.toLowerCase().contains(query.toLowerCase()) ||
            exchange.teluguText.toLowerCase().contains(query.toLowerCase()),
      );

      return titleMatch || categoryMatch || contentMatch;
    }).toList();
  }

  Category? getCategoryByName(String name) {
    return _categories.firstWhere((category) => category.name == name);
  }

  Future<Conversation> getConversationWithCustomNames(
    Conversation originalConversation,
  ) async {
    final speakerNames = await PreferencesService.getSpeakerNames();

    final updatedExchanges = originalConversation.exchanges.map((exchange) {
      final customName = speakerNames[exchange.speaker] ?? exchange.speaker;
      return SpeakerExchange(
        speaker: customName,
        englishText: exchange.englishText,
        teluguText: exchange.teluguText,
      );
    }).toList();

    return Conversation(
      title: originalConversation.title,
      category: originalConversation.category,
      exchanges: updatedExchanges,
      filePath: originalConversation.filePath,
    );
  }

  Future<List<Category>> getCategoriesWithCustomNames() async {
    final speakerNames = await PreferencesService.getSpeakerNames();

    return _categories.map((category) {
      final updatedConversations = category.conversations.map((conversation) {
        final updatedExchanges = conversation.exchanges.map((exchange) {
          final customName = speakerNames[exchange.speaker] ?? exchange.speaker;
          return SpeakerExchange(
            speaker: customName,
            englishText: exchange.englishText,
            teluguText: exchange.teluguText,
          );
        }).toList();

        return Conversation(
          title: conversation.title,
          category: conversation.category,
          exchanges: updatedExchanges,
          filePath: conversation.filePath,
        );
      }).toList();

      return Category(name: category.name, conversations: updatedConversations);
    }).toList();
  }
}
