function f(n)
{
	let answer = 1;
	for (let i = 2; i < n; i++)
	{
		answer *= i;
	}
	return answer;
}