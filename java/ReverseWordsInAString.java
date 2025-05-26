import java.util.ArrayList;

public class ReverseWordsInAString {
  public static void main(String[] args) {
    System.out.println(run("the sky is blue"));
    System.out.println(run("  hello world  "));
    System.out.println(run("a good   example"));
  }

  static String run(String s) {
    var words = new ArrayList<String>();
    var n = s.length();
    var i = 0;

    while(i < n) {
      if (s.charAt(i) == ' ') {
        i++;
        continue;
      }

      var word = "";
      while (i < n && s.charAt(i) != ' ') {
        word += s.charAt(i++);
      }
      words.add(word);
    }

    var ans = new ArrayList<String>();
    for (int j = words.size() - 1; j >= 0; j--) {
      ans.add(words.get(j));
    }

    return String.join(" ", ans);
  }
}
