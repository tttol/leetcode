import java.util.Arrays;

public class StringCompression {
  public static void main(String[] args) {
    System.out.println(run(new char[] {'a','a','a','b','b','a','a'}));
    System.out.println(run(new char[] {'a','a','b','b','c','c','c'}));
    System.out.println(run(new char[] {'a'}));
    System.out.println(run(new char[] {'a','b','b','b','b','b','b','b','b','b','b','b','b'}));
  }

  static int run(char[] chars) {
    var n = chars.length;
    var currentIndex = 0;
    var resultIndex = 0;

    while (currentIndex < n) {
      var currentChar = chars[currentIndex];
      var count = 0;
      while (currentIndex < n && currentChar == chars[currentIndex]) {
        count++;
        currentIndex++;
      }
      
      chars[resultIndex++] = currentChar;
      if (count > 1) {
        var countStr = String.valueOf(count);
        for (int j = 0; j < countStr.length(); j++) {
          chars[resultIndex++] = countStr.charAt(j);
        }
      }
    }

    System.out.println(Arrays.toString(chars));

    return resultIndex;
  }
}
