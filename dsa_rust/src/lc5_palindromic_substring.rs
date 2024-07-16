fn find_palindrome(s: String) -> String {
    let chars: Vec<char> = s.chars().collect();
    let mut max_len = 0;
    let mut max_s = String::new();
    let len = chars.len() as i32;

    for i in 0..len{
        let mut j = i;
        let mut k = i;
        while k < len && j >= 0 && chars[j as usize] == chars[k as usize] {
            if k - j + 1 > max_len {
                max_len = k - j + 1;
                max_s = chars[j as usize..=k as usize].iter().collect();
            } 
            j -= 1;
            k += 1; 
        }

        let mut j = i;
        let mut k = i+1;
        while j >= 0 && k < len && chars[j as usize] == chars[k as usize] {
            if k - j + 1 > max_len {
                max_len = k - j + 1;
                max_s = chars[j as usize..=k as usize].iter().collect();
            } 
            j -= 1;
            k += 1; 
        }
    }
    max_s
}


pub fn longest_palindromic_substring() {
    let s = String::from("babad");
    let result = find_palindrome(s);
    println!("{result}");
}


#[cfg(test)]
mod tests {
    use crate::lc5_palindromic_substring::find_palindrome;

    #[test]
    fn test1 () {
        let s = String::from("babad");
        assert_eq!("bab".to_string(), find_palindrome(s))
    }
    #[test]
    fn test2 () {
        let s = String::from("cbbd");
        assert_eq!("bb".to_string(), find_palindrome(s))
    }
}
