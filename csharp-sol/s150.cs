namespace csharp_sol 
{
    public static class S150 
    {
        public static int EvalRPN(string[] tokens) 
        {
            
            Stack<string> stack = [];
            Dictionary<string, Func<int, int, int>> map = new()
            {
                {"+", (x,y) => x+y},
                {"-", (x,y) => x-y},
                {"*", (x,y) => x*y},
                {"/", (x,y) => x/y},
            };
            for (int i = 0; i < tokens.Length; i++)
            {
                if (!map.ContainsKey(tokens[i]))
                {
                    stack.Push(tokens[i]);
                }
                else
                {
                    int b = Int32.Parse(stack.Pop());
                    int a = Int32.Parse(stack.Pop());
                    int res = map[tokens[i]](a, b);
                    stack.Push(res.ToString());
                }
            }
            return int.Parse(stack.Pop());
        }

    }
}
