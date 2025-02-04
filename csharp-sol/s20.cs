namespace csharp_sol 
{
    public static class S20 
    {
        public static bool IsValid(string s) 
        {
            
            Dictionary<char, char> close_to_open = new()
            {
                {')', '('},
                {']', '['},
                {'}', '{'}
            };
            Stack<char> stack = [];
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i] == '(' || s[i] == '[' || s[i] == '{') 
                {
                    stack.Push(s[i]);
                    continue;   
                }
                else if (stack.Count != 0 && stack.Peek() == close_to_open[s[i]])
                {
                    stack.Pop();
                }
                else
                {
                    return false;
                }
            }

            return stack.Count == 0;
        }
    }
}
