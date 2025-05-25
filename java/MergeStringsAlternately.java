public class MergeStringsAlternately {
  public static void main(String[] args) {
    System.out.println(run("abc", "pqr"));
    System.out.println(run("ab", "pqrs"));
    System.out.println(run("abcd", "pq"));
  }

  static String run(String word1, String word2) {
    var n1 = word1.length();
    var n2 = word2.length();
    var n = Math.max(n1, n2);
    var i = 0;
    var ans = "";
    while (i < n) {
      if (i < n1) {
        ans += word1.charAt(i);
      }
      
      if (i < n2) {
        ans += word2.charAt(i);
      }
      i++;
    }
    return ans;
    }
}
