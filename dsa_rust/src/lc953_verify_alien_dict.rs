use std::collections::HashMap;

fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
    let mut word_order: HashMap<char, i32> = HashMap::new();
    for (i,c) in order.chars().enumerate() {
        word_order.insert(c, i as i32);
    }

    for i in 0..words.len()-1 {
        let word1: Vec<char> = words[i].chars().collect();
        let word2: Vec<char> = words[i+1].chars().collect();

        for j in 0..word1.len() {
            if j == word2.len() {
                return false
            }
            if word1[j] != word2[j] {
                if word_order.get(&word1[j]).unwrap() > word_order.get(&word2[j]).unwrap() {
                    return false
                } break;
            }
        }
    }
    // println!("{:?}", word_order);
    true
}

pub fn sort_alien_dict() {
    let words: Vec<String> = vec![String::from("hello"),String::from("leetcode")];
    let order = String::from("hlabcdefgijkmnopqrstuvwxyz");
    let result = is_alien_sorted(words, order);
    println!("{result}");
}

#[cfg(test)]
mod tests {
    use crate::lc953_verify_alien_dict::is_alien_sorted;

    #[test]
    fn test1() {
    let words: Vec<String> = vec![String::from("word"),String::from("world"),String::from("row")];
    let order = String::from("worldabcefghijkmnpqstuvxyz");
    assert_eq!(false, is_alien_sorted(words, order));
    }

    #[test]
    fn test2() {
    let words: Vec<String> = vec![String::from("hello"),String::from("leetcode")];
    let order = String::from("hlabcdefgijkmnopqrstuvwxyz");
    assert_eq!(true, is_alien_sorted(words, order));
    }

    #[test]
    fn test3() {
    let words: Vec<String> = vec![String::from("apple"),String::from("app")];
    let order = String::from("abcdefghijklmnopqrstuvwxyz");
    assert_eq!(false, is_alien_sorted(words, order));
    }
}
