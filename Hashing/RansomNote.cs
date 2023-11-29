public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {
        var magazineLetters = new Dictionary<char, int>(); // the string is the character, and the int is the number of times it appears and can be used
        
        for (var i = 0; i < magazine.Length; ++i)
        {
            if (!magazineLetters.ContainsKey(magazine[i])) 
            {
                magazineLetters.Add(magazine[i], 0);
            }
            
            magazineLetters[magazine[i]] += 1; // increase the number of times the letter can be used
        }
        
        for (var i = 0; i < ransomNote.Length; ++i)
        {
            if (!magazineLetters.ContainsKey(ransomNote[i]))
            {
                return false; // letter doesn't exist
            }
            
            magazineLetters[ransomNote[i]] -= 1;
        }
        
        foreach (int charCount in magazineLetters.Values)
        {
            if (charCount < 0)
            {
                return false;
            }
        }
        
        return true;
    }
}