use std::collections::VecDeque;

fn count_islands(mut grid: Vec<Vec<char>>) -> i32 {
    let m = grid.len();
    let n = grid[0].len();
    let mut q: VecDeque<(usize,usize)> = VecDeque::with_capacity(m * n);
    let mut num_islands = 0;

    for i in 0..m {
        for j in 0..n {
            if grid[i][j] == '1' {
                q.push_back((i,j));
                num_islands += 1;

                while !q.is_empty() {
                    for _ in 0..q.len() {
                        let (k,l) = q.pop_front().unwrap();
                        if k < m && l < n && grid[k][l] == '1' {
                            grid[k][l] = '0';
                            for w in [0,1,0,!0,0].windows(2) {
                                q.push_back((k.wrapping_add(w[0]), l.wrapping_add(w[1])));
                            }
                        }
                    }
                }
            }
        }
    }
    num_islands
}


pub fn num_islands() {
    let grid= vec![
              vec!['1','1','1','1','0'],
              vec!['1','1','0','1','0'],
              vec!['1','1','0','0','0'],
              vec!['0','0','0','0','0']
            ];
    let result = count_islands(grid);
    println!("{result}");
}
