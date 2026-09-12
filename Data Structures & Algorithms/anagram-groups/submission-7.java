class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> temp = new HashMap();

        for(int i=0; i<strs.length; i++){
            int[] keys = new int[26];
            for (int j = 0; j < strs[i].length(); j++) {
                keys[(int)(strs[i].charAt(j))-'a']+=1;
            }
            String hello = Arrays.toString(keys);
            if(!temp.containsKey(hello)) {
                temp.put(hello, new ArrayList<>());
                temp.get(hello).add(strs[i]);
            }
            else{
                temp.get(hello).add(strs[i]);
            }
        }

        
        return new ArrayList<>(temp.values());

    }
}
