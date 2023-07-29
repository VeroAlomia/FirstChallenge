class Solution(object):
    def mergeArrays(self, nums1, nums2):
        out, d2 = dict(nums1), dict(nums2)  #Asignación de dos variables al mismo tiempo
        for k in d2:
            out[k] = out[k]+ d2[k] if out.get(k) else d2[k] #ternario #out.get(k) 
        return [[k,out[k]] for k in sorted(out)]