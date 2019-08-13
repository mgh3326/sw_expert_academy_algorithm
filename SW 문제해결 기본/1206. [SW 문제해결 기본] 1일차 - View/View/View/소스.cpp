#include<iostream>
#include<deque>
using namespace std;
int main(void) {
	int test_num = 10;// 10개가 주어진다고 먼저 알려줬다.
	for (int i = 0; i < test_num; i++)
	{
		int test_case_length = 0;
		scanf("%d", &test_case_length);
		deque<int> dq;
		int count = 0;

		for (int j = 0; j < test_case_length; j++)
		{

			int input = 0;
			scanf("%d", &input);
			dq.push_back(input);
			if (dq.size() == 5)
			{
				int dq_max = dq.at(0);
				for (int k = 1; k < 5; k++)
				{
					if (k == 2)
						continue; //얘는 안봐
					if (dq_max < dq.at(k))
					{
						dq_max = dq.at(k);
					}
				}

				if (dq_max < dq.at(2))
				{
					count += dq.at(2) - dq_max;

				}
				dq.pop_front();


			}

		}
		printf("#%d %d\n", i + 1, count);

	}
	return 0;
}