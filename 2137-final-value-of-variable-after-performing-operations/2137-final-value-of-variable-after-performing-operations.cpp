class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        
        for (int i = 0; i < operations.size(); i++) {
            switch (operations[i][1]) {
                case '+':
                    x++;
                    break;
                case '-':
                    x--;
                    break;
            }
        }
        
        return x;

    }
};