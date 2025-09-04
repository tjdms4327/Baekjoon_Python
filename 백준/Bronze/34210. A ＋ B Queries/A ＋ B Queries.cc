#include <vector>
using namespace std;

vector<int> A, B;

void initialize(vector<int> a, vector<int> b) {
    A = a;
    B = b;
}

int answer_question(int i, int j) {
    return A[i] + B[j];
}
