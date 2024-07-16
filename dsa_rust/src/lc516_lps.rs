use std::cmp::max;

fn longest_palindromic_subsequence(text: String) -> i32 {
    let n = text.len();
    let text1: Vec<char> = text.chars().collect();
    let text2: Vec<char> = text.chars().rev().collect();
    let mut dp = vec![vec![0;n+1];n+1];

    for i in (0..n).rev() {
        for j in (0..n).rev() {
           if text1[j] == text2[i] {
               dp[i][j] = 1 + dp[i+1][j+1];
           } 
           else {
               dp[i][j] = max(dp[i+1][j], dp[i][j+1]);
           }
        }
    }
    dp[0][0]
}


pub fn lps() {
    let text1 = String::from("bbbab");
    let result = longest_palindromic_subsequence(text1);
    println!("{result}");
}


#[cfg(test)]
mod tests {
    use crate::lc516_lps::longest_palindromic_subsequence;


    #[test]
    fn test1() {
        assert_eq!(4, longest_palindromic_subsequence("bbbab".to_string()));
    }
    #[test]
    fn test2() {
        assert_eq!(2, longest_palindromic_subsequence("cbbd".to_string()));
    }
}
