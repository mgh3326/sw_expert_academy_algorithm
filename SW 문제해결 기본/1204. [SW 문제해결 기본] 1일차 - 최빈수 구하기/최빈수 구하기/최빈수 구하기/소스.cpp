#include<iostream>
#include <algorithm>

int main(void)
{

	int test_num = 0;
	scanf("%d", &test_num);
	for (int i = 0; i < test_num; i++)
	{
		int array[101] = { 0 };

		int index = 0;
		scanf("%d", &index);
		int temp = 0;
		for (int j = 0; j < 1000; j++)
		{
			scanf("%d", &temp);
			array[temp]++;
		}
		int max = 0;
		int max_index = 0;
		for (int j = 100; j >= 0; j--)
		{
			if (max < array[j])
			{
				max = array[j];
				max_index = j;
			}
		}
		std::cout << "#" << index << " " << max_index << std::endl;

	}
	return 0;
}