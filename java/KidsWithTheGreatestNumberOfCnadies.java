import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class KidsWithTheGreatestNumberOfCnadies {
  public static void main(String[] args) {
    System.out.println(run(new int[]{2,3,5,1,3}, 3));
    System.out.println(run(new int[]{4,2,1,1,2}, 1));
    System.out.println(run(new int[]{12,1,12}, 10));
  }

  static List<Boolean> run(int[] candies, int extraCandies) {
    var max = Arrays.stream(candies).max();
    var ans = new ArrayList<Boolean>();
    for (var c : candies) {
      ans.add(max.getAsInt() <= c + extraCandies);
    }
    return ans;
  }
}
