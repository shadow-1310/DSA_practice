fn find_anagram(s: String, p: String) -> Vec<i32> {
    let s: Vec<char> = s.chars().collect();
    let p: Vec<char> = p.chars().collect();
    let len_p = p.len() as i32;
    let len_s = s.len() as i32;
    let mut result: Vec<i32> = Vec::new();

    if len_p > len_s {
        return result
    }

    let mut curr = [0;26];
    let mut target = [0;26];

    for i in 0..len_p {
        let idx1 = s[i as usize].to_ascii_lowercase() as i32 - 'a'.to_ascii_lowercase() as i32;
        let idx2 = p[i as usize].to_ascii_lowercase() as i32 - 'a'.to_ascii_lowercase() as i32;

        curr[idx1 as usize] += 1;
        target[idx2 as usize] += 1;
    }

    if curr == target {
        result.push(0);
    }

    let mut left = 0;
    let mut right = len_p;

    while right < len_s {
        let rem = s[left as usize].to_ascii_lowercase() as i32 - 'a'.to_ascii_lowercase() as i32;
        let add = s[right as usize].to_ascii_lowercase() as i32 - 'a'.to_ascii_lowercase() as i32;

        curr[rem as usize] -= 1;
        curr[add as usize] += 1;

        if curr == target {
            result.push(left+1);
        }
        left += 1;
        right += 1;
    }
    result
}

pub fn find_all_anagrams() {
    let s = String::from("cbaebabacd");
    let p = String::from("abc");

    let result = find_anagram(s, p);
    println!("{:?}", result);
}

#[cfg(test)]
mod tests {
    use crate::lc438_all_anagrams::find_anagram;

    #[test]
    fn test1() {
    let s = String::from("cbaebabacd");
    let p = String::from("abc");
    assert_eq!(vec![0,6], find_anagram(s, p));
    }

    #[test]
    fn test2() {
    let s = String::from("abab");
    let p = String::from("ab");
    assert_eq!(vec![0,1,2], find_anagram(s, p));
    }

    #[test]
    fn test3() {
    let s = String::from("aaaaaaaaaa");
    let p = String::from("aaaaaaaaaaaaa");
    assert_eq!(vec![0;0], find_anagram(s, p));
    }
}
