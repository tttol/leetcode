import java.util.ArrayList;
import java.util.List;

public class ReverseVowelsOfAString {

  public static void main(String[] args) {
    System.out.println(run("IceCreAm"));
    System.out.println(run("leetcode"));
  }

  static String run(String s) {
    var VOWELS = List.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
    var vowels = new ArrayList<Character>();

    for (int i = 0; i < s.length(); i++) {
      if (VOWELS.contains(s.charAt(i))) {
        vowels.add(s.charAt(i));
      }
    }
    
    var ans = "";
    var vowelsIndex = vowels.size() - 1;
    for (int i = 0; i < s.length(); i++) {
      if (VOWELS.contains(s.charAt(i))) {
        ans += vowels.get(vowelsIndex--);
      } else {
        ans += s.charAt(i);
      }
    }

    return ans;
  }
}