public class CanPlaceFLowers {
  public static void main(String[] args) {
    // System.out.println(run(new int[] {1,0,0,0,1}, 1));
    // System.out.println(run(new int[] {1,0,0,0,1}, 2));
    System.out.println(run(new int[] {1}, 0));
    System.out.println(run(new int[] {0}, 1));
  }

  static boolean run(int[] flowerbed, int n) {
    var len = flowerbed.length;
    var count = 0;
    if (len == 1) {
      if (flowerbed[0] == 0) {
        count++;
      }
      return count >= n;
    }

    for (var i = 0; i < len; i++) {
      if (i == 0) {
        if (flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
          flowerbed[i] = 1;
          count++;
        }
      } else if(i > 0 && i < len - 1) {
        if ((flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0)) {
          flowerbed[i] = 1;
          count++;
        }
      } else if (i == len - 1) {
        if (flowerbed[i - 1] == 0 && flowerbed[i] == 0) {
          flowerbed[i] = 1;
          count++;
        }
      }
      if (count >= n) return true;
    }
    return false;
  }
}
