public class CodeSignalSample {
    public static void main(String[] args) {
        System.out.println(solution(29));
        System.out.println(solution(50));
        System.out.println(solution(10));

    }

    static int solution(int n) {
        int ans = 0;
        while (n > 0) {
            ans += n % 10;
            n /= 10;
        }
        return ans;
    }
}