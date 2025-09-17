import 'package:flutter/material.dart';
import '../models/conversation.dart';
import '../services/html_parser.dart';
import 'conversation_screen.dart';

class CategoryScreen extends StatelessWidget {
  final Category category;

  const CategoryScreen({super.key, required this.category});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(HtmlParserService.getCategoryDisplayName(category.name)),
        backgroundColor: Theme.of(context).colorScheme.primaryContainer,
        foregroundColor: Theme.of(context).colorScheme.onPrimaryContainer,
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: category.conversations.length,
        itemBuilder: (context, index) {
          final conversation = category.conversations[index];
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              contentPadding: const EdgeInsets.all(16),
              title: Text(
                conversation.title,
                style: Theme.of(
                  context,
                ).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold),
              ),
              subtitle: Padding(
                padding: const EdgeInsets.only(top: 8),
                child: Text(
                  'Speakers: ${conversation.exchanges.map((e) => e.speaker).toSet().join(', ')}',
                  style: Theme.of(context).textTheme.bodyMedium,
                ),
              ),
              trailing: Icon(
                Icons.arrow_forward_ios,
                size: 16,
                color: Theme.of(context).colorScheme.primary,
              ),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) =>
                        ConversationScreen(conversation: conversation),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}
