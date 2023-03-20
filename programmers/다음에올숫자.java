class Solution {

  public int sameDiffer(int[] common) {
    int one = common[1] - common[0];
    int two = common[2] - common[1];

    if (one == two) {
      return common[common.length - 1] + one;
    } else {
      return common[common.length - 1] * common[1] / common[0];
    }
  }

  public int solution(int[] common) {
    return sameDiffer(common);
  }
}
