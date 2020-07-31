#include <iostream>
#include <string>
#include <deque>
using namespace std;

int main(void)

{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    
    deque<int> dq;
    
    for (int i = 0; i < N; i++){
        
        string temp;
        cin >> temp;
        int num;
        
        if (temp == "push_back"){
            
            cin >> num;
            dq.push_back(num);
            }
        
        else if (temp == "push_front"){
            
            cin >> num;
            dq.push_front(num);
            }

        else if (temp == "pop_front"){
            
            if (dq.empty()) cout << -1 << "\n";
            else{
                cout << dq.front() << "\n";
                dq.pop_front();
                }
            }

        else if (temp == "pop_back"){
            
            if (dq.empty()) cout << -1 << "\n";
            else{
                cout << dq.back() << "\n";
                dq.pop_back();
                }

            }

        else if (temp == "size"){
            
            cout << dq.size() << "\n";

            }

        else if (temp == "empty"){
            
            if (dq.empty()) cout << 1 << "\n";
            else cout << 0 << "\n";

            }

        else if (temp == "front"){
            
            if (dq.empty())
            cout << -1 << "\n";
            else cout << dq.front() << "\n";

            }

        else if (temp == "back"){
            
            if (dq.empty()) cout << -1 << "\n";
            else

                                 cout << dq.back() << "\n";

                 }

        }

        return 0;

}