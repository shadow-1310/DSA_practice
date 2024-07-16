use std::cmp::max;
fn longest_subarray(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
    let len1 = nums1.len();
    let len2 = nums2.len();
    let mut dp: Vec<Vec<i32>> = vec![vec![0;len2+1];len1+1];

    for i in (0..len1).rev() {
        for j in (0..len2).rev() {
            // println!("{i},{j}");
            if nums1[i] == nums2[j] {
                dp[i][j] = 1 + dp[i+1][j+1];
            }
        }
    }
    // println!("{:?}", dp);
    let mut max_val = 0;
    for i in 0..len1 {
        for j in 0..len2 {
            max_val = max(max_val, dp[i][j]);
        }
    }
    max_val
}


pub fn find_length() {
    let nums1: Vec<i32> = vec![1,2,3,2,1];
    let nums2: Vec<i32> = vec![3,2,1,4,7];
    let result = longest_subarray(nums1, nums2);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use crate::lc718_longest_subarray::longest_subarray;

    #[test]
    fn test1() {
    let nums1 = vec![1,2,3,2,1];
    let nums2 = vec![3,2,1,4,7];
    assert_eq!(3, longest_subarray(nums1, nums2));
    }

    #[test]
    fn test2() {
    let nums1 = vec![0,0,0,0,0];
    let nums2 = vec![0,0,0,0,0];
    assert_eq!(5, longest_subarray(nums1, nums2));
    }

    #[test]
    fn test3() {
    let nums1 = vec![1,0,0,0,1];
    let nums2 = vec![1,0,0,1,1];
    assert_eq!(3, longest_subarray(nums1, nums2));
    }
}
