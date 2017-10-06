class Solution {
public:
    /*
     * @param source: source string to be scanned.
     * @param target: target string containing the sequence of characters to match
     * @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
     */
    int strStr(const char *source, const char *target) {
        // write your code here
    int source_length=0,target_length=0;
    int source_count=0,target_count=0;
    int correct=0;
    source_length=strlen(source);
    target_length=strlen(target);
    
    if(source_length==0 && target_length==0)
        return 0;
    if(source_length==0)
        return -1;

    for(source_count=0;source_count+target_length<=source_length;source_count++)
    {
      for(target_count=0,correct=0;target_count<target_length;target_count++)  
      {
          if(target[target_count]==NULL)  
              return -1;
          if(source[source_count+target_count]==target[target_count])
              correct++; 
      }
      if(correct==target_length)
        return source_count;
    }
    return -1;
    }
};
