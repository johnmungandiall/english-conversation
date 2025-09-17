import 'package:shared_preferences/shared_preferences.dart';

class PreferencesService {
  static const String _speaker1NameKey = 'speaker1_name';
  static const String _speaker2NameKey = 'speaker2_name';

  static const String _defaultSpeaker1Name = 'John';
  static const String _defaultSpeaker2Name = 'Giri';

  static Future<String> getSpeaker1Name() async {
    try {
      final prefs = await SharedPreferences.getInstance().timeout(
        const Duration(seconds: 5),
        onTimeout: () => throw Exception('SharedPreferences timeout'),
      );
      return prefs.getString(_speaker1NameKey) ?? _defaultSpeaker1Name;
    } catch (e) {
      print('Error getting speaker1 name: $e');
      return _defaultSpeaker1Name;
    }
  }

  static Future<String> getSpeaker2Name() async {
    try {
      final prefs = await SharedPreferences.getInstance().timeout(
        const Duration(seconds: 5),
        onTimeout: () => throw Exception('SharedPreferences timeout'),
      );
      return prefs.getString(_speaker2NameKey) ?? _defaultSpeaker2Name;
    } catch (e) {
      print('Error getting speaker2 name: $e');
      return _defaultSpeaker2Name;
    }
  }

  static Future<void> setSpeaker1Name(String name) async {
    try {
      final prefs = await SharedPreferences.getInstance().timeout(
        const Duration(seconds: 5),
        onTimeout: () => throw Exception('SharedPreferences timeout'),
      );
      await prefs.setString(
        _speaker1NameKey,
        name.trim().isEmpty ? _defaultSpeaker1Name : name.trim(),
      );
    } catch (e) {
      print('Error setting speaker1 name: $e');
      // Continue without throwing to avoid breaking the UI
    }
  }

  static Future<void> setSpeaker2Name(String name) async {
    try {
      final prefs = await SharedPreferences.getInstance().timeout(
        const Duration(seconds: 5),
        onTimeout: () => throw Exception('SharedPreferences timeout'),
      );
      await prefs.setString(
        _speaker2NameKey,
        name.trim().isEmpty ? _defaultSpeaker2Name : name.trim(),
      );
    } catch (e) {
      print('Error setting speaker2 name: $e');
      // Continue without throwing to avoid breaking the UI
    }
  }

  static Future<Map<String, String>> getSpeakerNames() async {
    final speaker1 = await getSpeaker1Name();
    final speaker2 = await getSpeaker2Name();
    return {_defaultSpeaker1Name: speaker1, _defaultSpeaker2Name: speaker2};
  }

  static Future<void> resetToDefaults() async {
    try {
      await setSpeaker1Name(_defaultSpeaker1Name);
      await setSpeaker2Name(_defaultSpeaker2Name);
    } catch (e) {
      print('Error resetting to defaults: $e');
      // Continue without throwing to avoid breaking the UI
    }
  }
}
