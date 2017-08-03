namespace Ex{
    using System;
    public static class Exclass{
        public static int BinarySearch<T>(this T[] array, T target) where T : IComparable<T>{
            int min = 0;
            int max = array.Length - 1;
        
            while (true)
            {
                if (max < min) return -1;
                int mid = min + (max - min) / 2;
                switch (target.CompareTo(array[mid]))
                {
                    case -1:
                        max = mid - 1;
                        break;
                    case 1:
                        min = mid + 1;
                        break;
                    case 0:
                        return mid;
                }
            }
        }
        
        public static int UpperBound<T>(this T[] array, T target) where T : IComparable<T>{
            int low = 0;
            int high = array.Length-1;
            int mid;
            if(target.CompareTo(array[high])>0) return -1;
            while (low<high){
                mid = (low+high)/2;
                if(array[mid].CompareTo(target)<0) low=mid+1;
                else high = mid;
            }
            return low;
        }
    
        public static int LowerBound<T>(this T[] array, T target) where T : IComparable<T>{
            int low = 0;
            int high = array.Length-1;
            int mid;
            if(target.CompareTo(array[0])<0) return -1;
            while (low<high){
                mid = (low+high)/2;
                if(array[mid].CompareTo(target)<=0)low = mid+1;
                else high = mid;
            }
            if(low==high)low--;
            if(low.CompareTo(array[0]<0)) return -1;
            return low;
        }
    }
}
