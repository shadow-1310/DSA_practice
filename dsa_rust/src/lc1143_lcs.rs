use std::cmp::max;

fn longest_common_subsequence(text1: String, text2: String) -> i32 {
    println!("Finding LCS for string 1: {} and string2: {}", text1, text2);
    let text1: Vec<char> = text1.chars().collect();
    let text2: Vec<char> = text2.chars().collect();
    let mut map = vec![vec![0;text1.len()+1]; text2.len()+1];

    for j in (0..text1.len()).rev() {
        for i in (0..text2.len()).rev() {
            if text1[j] == text2[i] {
                map[i][j] = 1 + map[i+1][j+1];
            } else {
                map[i][j] = max(map[i+1][j], map[i][j+1]);
            }

        }
    }
    map[0][0]
    }
pub fn lcs() { 
    let text1 = String::from("abcde");
    let text2 = String::from("ace");
    let result = longest_common_subsequence(text1, text2);
    println!("{result}")
}


#[cfg(test)]
mod tests {
    use crate::lc1143_lcs::longest_common_subsequence;

    #[test]
    fn test1() {
        assert_eq!(3, longest_common_subsequence("abcde".to_string(), "ace".to_string()));
    }
    #[test]
    fn test2() {
        assert_eq!(3, longest_common_subsequence("abc".to_string(), "abc".to_string()));
    }
    #[test]
    fn test3() {
        assert_eq!(0, longest_common_subsequence("abc".to_string(), "def".to_string()));
    }
}
