class SpeakerExchange {
  final String speaker;
  final String englishText;
  final String teluguText;

  SpeakerExchange({
    required this.speaker,
    required this.englishText,
    required this.teluguText,
  });

  factory SpeakerExchange.fromMap(Map<String, dynamic> map) {
    return SpeakerExchange(
      speaker: map['speaker'] ?? '',
      englishText: map['englishText'] ?? '',
      teluguText: map['teluguText'] ?? '',
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'speaker': speaker,
      'englishText': englishText,
      'teluguText': teluguText,
    };
  }
}

class Conversation {
  final String title;
  final String category;
  final List<SpeakerExchange> exchanges;
  final String filePath;

  Conversation({
    required this.title,
    required this.category,
    required this.exchanges,
    required this.filePath,
  });

  factory Conversation.fromMap(Map<String, dynamic> map) {
    return Conversation(
      title: map['title'] ?? '',
      category: map['category'] ?? '',
      exchanges: (map['exchanges'] as List<dynamic>?)
          ?.map((e) => SpeakerExchange.fromMap(e as Map<String, dynamic>))
          .toList() ?? [],
      filePath: map['filePath'] ?? '',
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'title': title,
      'category': category,
      'exchanges': exchanges.map((e) => e.toMap()).toList(),
      'filePath': filePath,
    };
  }
}

class Category {
  final String name;
  final List<Conversation> conversations;

  Category({
    required this.name,
    required this.conversations,
  });

  factory Category.fromMap(Map<String, dynamic> map) {
    return Category(
      name: map['name'] ?? '',
      conversations: (map['conversations'] as List<dynamic>?)
          ?.map((e) => Conversation.fromMap(e as Map<String, dynamic>))
          .toList() ?? [],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'name': name,
      'conversations': conversations.map((e) => e.toMap()).toList(),
    };
  }
}
