class Solution:

    def encode(self, strs: List[str]) -> str:
        
        decoder = "#"
        for s in strs:
            decoder += f"{len(s)}/"
        decoder += "#"

        return decoder + "".join(strs)
        
    def decode(self, s: str) -> List[str]:
        idx_s = s[1:].index("#")
        decoder = s[1:idx_s].split("/")
        s = s[idx_s+2:]
        output = []
        print(decoder, s)
        if len(decoder) == 0 or decoder[0] == "" : return []
        for d in decoder:
            output.append(s[:int(d)])
            s = s[int(d):]

        return output
