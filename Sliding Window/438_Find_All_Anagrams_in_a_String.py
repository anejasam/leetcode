class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        result = []
        p_map, s_map = {}, {}
        
        for c in p:
            p_map[c] = p_map.get(c, 0) + 1
        
        for i,c in enumerate(s):
            start_index = i - len(p)
                
            if i >= len(p):
                start_value = s[start_index]
                s_map[start_value] -= 1
                if s_map[start_value] == 0:
                    del s_map[start_value]
            
            s_map[c] = s_map.get(c,0) + 1
            
            if p_map == s_map:
                result.append(start_index + 1)
                
        return result
                

