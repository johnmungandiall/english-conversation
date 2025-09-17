import 'package:flutter/material.dart';
import '../models/conversation.dart';
import '../services/preferences_service.dart';

class ConversationScreen extends StatefulWidget {
  final Conversation conversation;

  const ConversationScreen({super.key, required this.conversation});

  @override
  State<ConversationScreen> createState() => _ConversationScreenState();
}

class _ConversationScreenState extends State<ConversationScreen> {
  bool _showEnglish = true;
  bool _showTelugu = true;
  late Conversation _conversationWithCustomNames;
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadConversationWithCustomNames();
  }

  Future<void> _loadConversationWithCustomNames() async {
    final speakerNames = await PreferencesService.getSpeakerNames();

    final updatedExchanges = widget.conversation.exchanges.map((exchange) {
      final customName = speakerNames[exchange.speaker] ?? exchange.speaker;
      return SpeakerExchange(
        speaker: customName,
        englishText: exchange.englishText,
        teluguText: exchange.teluguText,
      );
    }).toList();

    setState(() {
      _conversationWithCustomNames = Conversation(
        title: widget.conversation.title,
        category: widget.conversation.category,
        exchanges: updatedExchanges,
        filePath: widget.conversation.filePath,
      );
      _isLoading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return Scaffold(
        appBar: AppBar(
          title: Text(widget.conversation.title),
          backgroundColor: Theme.of(context).colorScheme.primaryContainer,
          foregroundColor: Theme.of(context).colorScheme.onPrimaryContainer,
        ),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: Text(_conversationWithCustomNames.title),
        backgroundColor: Theme.of(context).colorScheme.primaryContainer,
        foregroundColor: Theme.of(context).colorScheme.onPrimaryContainer,
        actions: [
          PopupMenuButton<String>(
            onSelected: (value) {
              setState(() {
                switch (value) {
                  case 'english_only':
                    _showEnglish = true;
                    _showTelugu = false;
                    break;
                  case 'telugu_only':
                    _showEnglish = false;
                    _showTelugu = true;
                    break;
                  case 'both':
                    _showEnglish = true;
                    _showTelugu = true;
                    break;
                }
              });
            },
            itemBuilder: (context) => [
              const PopupMenuItem(
                value: 'both',
                child: Text('Show Both Languages'),
              ),
              const PopupMenuItem(
                value: 'english_only',
                child: Text('English Only'),
              ),
              const PopupMenuItem(
                value: 'telugu_only',
                child: Text('Telugu Only'),
              ),
            ],
          ),
        ],
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: _conversationWithCustomNames.exchanges.length,
        itemBuilder: (context, index) {
          final exchange = _conversationWithCustomNames.exchanges[index];
          return Card(
            elevation: 2,
            margin: const EdgeInsets.only(bottom: 12),
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Speaker name
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 12,
                      vertical: 6,
                    ),
                    decoration: BoxDecoration(
                      color: Theme.of(context).colorScheme.primaryContainer,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Text(
                      exchange.speaker,
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: Theme.of(context).colorScheme.onPrimaryContainer,
                      ),
                    ),
                  ),
                  const SizedBox(height: 12),

                  // English text
                  if (_showEnglish && exchange.englishText.isNotEmpty) ...[
                    Text(
                      exchange.englishText,
                      style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: Theme.of(context).colorScheme.onSurface,
                      ),
                    ),
                    if (_showTelugu && exchange.teluguText.isNotEmpty)
                      const SizedBox(height: 8),
                  ],

                  // Telugu text
                  if (_showTelugu && exchange.teluguText.isNotEmpty) ...[
                    Text(
                      exchange.teluguText,
                      style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: Theme.of(context).colorScheme.onSurfaceVariant,
                        fontFamily:
                            'Noto Sans Telugu', // Fallback font for Telugu
                      ),
                    ),
                  ],
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
