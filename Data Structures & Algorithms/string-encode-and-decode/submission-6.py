class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}"
        return encoded # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])

            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
        return decoded
