def solution(video_len, pos, op_start, op_end, commands):
    vl = int(video_len[:2]) * 60 + int(video_len[3:])
    ps = int(pos[:2]) * 60 + int(pos[3:])
    os = int(op_start[:2]) * 60 + int(op_start[3:])
    oe = int(op_end[:2]) * 60 + int(op_end[3:])
    print(vl,ps,os,oe)
    
        
    for c in commands:
        if ps >= os and ps < oe:
            ps = oe
        if c == "next":
            ps += 10
            if ps > vl:
                ps = vl
        if c == "prev":
            ps -= 10
            if ps < 0:
                ps = 0
    
    if ps >= os and ps < oe:
        ps = oe        
    m = ps // 60
    s = ps % 60
    
    return '%.2d:%.2d'%(m,s)
