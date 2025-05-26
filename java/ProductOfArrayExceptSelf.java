import java.util.ArrayList;
import java.util.Arrays;

public class ProductOfArrayExceptSelf {
  public static void main(String[] args) {
    var ans1 = run(new int[] {1,2,3,4});
    var ans2 = run(new int[] {-1,1,0,-3,3});

    Arrays.stream(ans1).forEach(a -> System.out.println(a));
    Arrays.stream(ans2).forEach(a -> System.out.println(a));
  }

  static int[] run(int[] nums) {
    var n = nums.length;
    var cumuratedProducts = new int[n];
    cumuratedProducts[0] = nums[0];
    var reverseCumuratedProducts = new int[n];
    reverseCumuratedProducts[n - 1] = nums[n - 1];

    for (int i = 1; i < n; i++) {
      cumuratedProducts[i] = cumuratedProducts[i - 1] * nums[i];
    }

    for (int i = n - 2; i >= 0; i--) {
      reverseCumuratedProducts[i] = reverseCumuratedProducts[i + 1] * nums[i];
    }

    var ans = new ArrayList<Integer>();
    for (int i = 0; i < n; i++) {
      if (i == 0) {
        ans.add(reverseCumuratedProducts[1]);
      } else if (i == n - 1) {
        ans.add(cumuratedProducts[n - 2]);
      } else {
        ans.add(cumuratedProducts[i - 1] * reverseCumuratedProducts[i + 1]);
      }
    }

    var result = new int[n];
    for (int i = 0; i < n; i++) {
      result[i] = ans.get(i);
    }
    return result;
  }
}
