use std::collections::HashMap;
use std::cmp::max;

fn find_substring(s: String) -> i32 {
    let chars: Vec<char> = s.chars().collect();
    let mut seen: HashMap<char, i32> = HashMap::new();
    let mut max_len = 0;
    let mut left = 0;
    let mut right = 0;
    let len = chars.len() as i32;

    while right < len && left < len {
        if seen.contains_key(&chars[right as usize]) && seen[&chars[right as usize]] >= left {
            left = seen[&chars[right as usize]] + 1;
        } else {
            max_len = max(max_len, right - left + 1);
        }
        seen.insert(chars[right as usize], right);
        right += 1;
    }

    max_len
}


pub fn length_of_longest_substring() {
    let s = String::from("pwwkew");
    let result = find_substring(s);
    println!("{result}");
}


#[cfg(test)]
mod tests {
    use crate::lc3_substring_no_repeat::find_substring;

    #[test]
    fn test1() {
    let s = String::from("abcabcbb");
    assert_eq!(3, find_substring(s));
    }

    #[test]
    fn test2() {
    let s = String::from("bbbbb");
    assert_eq!(1, find_substring(s));
    }

    #[test]
    fn test3() {
    let s = String::from("pwwkew");
    assert_eq!(3, find_substring(s));
    }

    #[test]
    fn test4() {
    let s = String::from("aab");
    assert_eq!(2, find_substring(s));
    }
}
