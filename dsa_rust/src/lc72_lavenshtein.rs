use std::cmp::min;

fn lavenshtein(text1: String, text2: String) -> i32 {
    let n1 = text1.len();
    let n2 = text2.len();
    let text1: Vec<char> = text1.chars().collect();
    let text2: Vec<char> = text2.chars().collect();
    let mut dp = vec![vec![0;n2+1];n1+1];
    
    for i in 0..n1+1 {
        dp[i][n2] = n1 - i;
    }

    for i in 0..n2+1 {
        dp[n1][i] = n2 - i;
    }

    for i in (0..n1).rev() {
        for j in (0..n2).rev() {
            if text1[i] == text2[j] {
                dp[i][j] = dp[i+1][j+1];
            } else {
                dp[i][j] = 1 + min(min(dp[i+1][j+1], dp[i+1][j]), dp[i][j+1]);
            }
        }
    }

    dp[0][0].try_into().unwrap()
}


pub fn edit_distance() {
    let text1 = String::from("horse");
    let text2 = String::from("ros");
    let result = lavenshtein(text1, text2);
    println!("lavenshtein distance is {}", result);
}


#[cfg(test)]
mod tests {
    use crate::lc72_lavenshtein::lavenshtein;

    #[test]
    fn test1() {
        let text1 = String::from("horse");
        let text2 = String::from("ros");
        assert_eq!(3, lavenshtein(text1, text2))
    }
    #[test]
    fn test2() {
        let text1 = String::from("intention");
        let text2 = String::from("execution");
        assert_eq!(5, lavenshtein(text1, text2))
    }
}
