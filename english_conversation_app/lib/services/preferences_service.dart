import 'package:shared_preferences/shared_preferences.dart';

class PreferencesService {
  static const String _speaker1NameKey = 'speaker1_name';
  static const String _speaker2NameKey = 'speaker2_name';

  static const String _defaultSpeaker1Name = 'John';
  static const String _defaultSpeaker2Name = 'Giri';

  static Future<String> getSpeaker1Name() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString(_speaker1NameKey) ?? _defaultSpeaker1Name;
  }

  static Future<String> getSpeaker2Name() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString(_speaker2NameKey) ?? _defaultSpeaker2Name;
  }

  static Future<void> setSpeaker1Name(String name) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(
      _speaker1NameKey,
      name.trim().isEmpty ? _defaultSpeaker1Name : name.trim(),
    );
  }

  static Future<void> setSpeaker2Name(String name) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(
      _speaker2NameKey,
      name.trim().isEmpty ? _defaultSpeaker2Name : name.trim(),
    );
  }

  static Future<Map<String, String>> getSpeakerNames() async {
    final speaker1 = await getSpeaker1Name();
    final speaker2 = await getSpeaker2Name();
    return {_defaultSpeaker1Name: speaker1, _defaultSpeaker2Name: speaker2};
  }

  static Future<void> resetToDefaults() async {
    await setSpeaker1Name(_defaultSpeaker1Name);
    await setSpeaker2Name(_defaultSpeaker2Name);
  }
}
