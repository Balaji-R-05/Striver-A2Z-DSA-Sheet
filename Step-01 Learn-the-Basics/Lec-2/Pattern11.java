public class Pattern11 {
    public static void main(String[] args) {
        int n = 5;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                System.out.print(((i+j)%2 == 1)? "0" : "1");
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}

// 1 
// 0 1
// 1 0 1
// 0 1 0 1
// 1 0 1 0 1