class Solution {
public:
    string predictPartyVictory(string senate) {
        int n = senate.length();
        queue <int> rad, dire;

        for (int i = 0; i < n; i++){
            if (senate[i] == 'R'){
                rad.push(i);
            }
            else {
                dire.push(i);
            }
        }

        while (!rad.empty() && !dire.empty()){
            if (rad.front() < dire.front()){
                rad.push(n++);
            }
            else{
                dire.push(n++);
            }
            rad.pop();
            dire.pop();

        }

        if (rad.empty()){
            return "Dire";
        }
        else{
            return "Radiant";
        }
        
    }
};