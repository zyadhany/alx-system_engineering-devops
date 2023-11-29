#include <bits/stdc++.h>
#include <unordered_map>

#define ll long long
#define ld long double
#define pl pair<ll, ll>
#define vi vector<ll>
#define vii vector<vi>
#define vc vector<char>
#define vcc vector<vc>
#define vp vector<pl>
#define mi map<ll,ll>
#define mc map<char,int>
#define sortx(X) sort(X.begin(),X.end());
#define all(X) X.begin(),X.end()
#define ln '\n'
#define YES {cout << "YES\n"; return;}
#define NO {cout << "NO\n"; return;}

using namespace std;

void req(vector<string> &X){
    ll re;
    string s = "";
    

    getline(cin, s);getline(cin, s);

    while (s.find("ENDSAGED") == string::npos)
    {
        re = 0;

        while (s[5 + re] != ' ')
            re++;
        
        s = s.substr (5, re);
        for (int i = 0; i < X.size(); i++)
        {
            if (X[i] == s) X[i] = "SAGED";
        }
        
        getline(cin, s);
    }
}

void solve(int tc) {
    string s = "";

    vector<string> X;

    cin >> s;
    while (s != "ENDSAGED")
    {
        X.push_back(s);
        cin >> s;
    }
    
    req(X);
    

    for (int i = 0; i < X.size(); i++)
    {
        if (X[i] != "SAGED")
            cout << X[i] << '\n';
    }
    
}

int main()
{
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int size = 1;

    //cin >> size;
    for (int i = 1; i <= size; i++)
        solve(i);
}
