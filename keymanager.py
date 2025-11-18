#!/usr/bin/env python3
# coding: UTF-8
import sys
l1_opy_ = sys.version_info [0] == 2
l11_opy_ = 2048
l111l_opy_ = 7
def l1l_opy_ (keyedStringLiteral):
    global l1lll_opy_
    stringNr = ord (keyedStringLiteral [-1])
    rotatedStringLiteral = keyedStringLiteral [:-1]
    rotationDistance = stringNr % len (rotatedStringLiteral)
    recodedStringLiteral = rotatedStringLiteral [:rotationDistance] + rotatedStringLiteral [rotationDistance:]
    if l1_opy_:
        stringLiteral = unicode () .join ([unichr (ord (char) - l11_opy_ - (charIndex + stringNr) % l111l_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    else:
        stringLiteral = str () .join ([chr (ord (char) - l11_opy_ - (charIndex + stringNr) % l111l_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    return eval (stringLiteral)
import os, sys, re
l11l1_opy_ = 40 + 1 + 9 + 4
l1l1l_opy_ = 0xFFFF
l11l_opy_ = re.compile(l1l_opy_ (u"ࠫࡤࡥࡖ࠴ࡆࡏࡣࡤ࠮࡛ࡢ࠯ࡩࡅ࠲ࡌ࠰࠮࠻ࡠࡿ࠶࠶ࠬ࠲࠲ࢀ࠭ࠬࠀ"))
def l111_opy_(key):
    if len(key) != l11l1_opy_:
        return False
    sum = 0
    for i in range(len(key) - 4):
        sum = sum + ord(key[i])
    l11ll_opy_ = sum % l1l1l_opy_
    l1111_opy_ = int(key[len(key)-4 : ], 16)
    return l11ll_opy_ == l1111_opy_
def check_key(key):
    return l111_opy_(key)
def verify(path):
    with open(path, l1l_opy_ (u"ࠬࡸࠧࠁ"), encoding=l1l_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬࠂ")) as l1l1_opy_:
        file = l1l1_opy_.read()
        match = l11l_opy_.search(file)
        if match and match.group(1) != l1l_opy_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫࠃ"):
            return True
        else:
            return False
def activate(path, key, l1llll_opy_=True):
    if l1llll_opy_ and not l111_opy_(key):
        return False
    ll_opy_ = l1l_opy_ (u"ࠨࡡࡢ࡚࠸ࡊࡌࡠࡡࠪࠄ") + key[0:10]
    file = None
    with open(path, l1l_opy_ (u"ࠩࡵࠫࠅ"), encoding=l1l_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩࠆ")) as l1l1_opy_:
        file = l1l1_opy_.read()
    with open(path, l1l_opy_ (u"ࠫࡼ࠭ࠇ"), encoding=l1l_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫࠈ"), newline=l1l_opy_ (u"࠭࡜࡯ࠩࠉ")) as l1ll1_opy_:
        l1ll1_opy_.write(l11l_opy_.sub(ll_opy_, file))
    return True
def deactivate(path):
    return activate(path, l1l_opy_ (u"ࠧ࠱࠲࠳࠴࠵࠶࠰࠱࠲࠳ࠫࠊ"), False)
if __name__ == l1l_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪࠋ"):
    l1ll_opy_ = sys.argv
    if len(l1ll_opy_) < 3:
        sys.exit(1)
    else:
        l1l11_opy_ = l1ll_opy_[1]
        if (l1l11_opy_ == l1l_opy_ (u"ࠩࡦ࡬ࡪࡩ࡫࠮࡭ࡨࡽࠬࠌ") or l1l11_opy_ == l1l_opy_ (u"ࠪࡧ࡭࡫ࡣ࡬ࡡ࡮ࡩࡾ࠭ࠍ")) and len(l1ll_opy_) == 3:
            if check_key(l1ll_opy_[2]):
                print(l1l_opy_ (u"ࠫࡔࡑࠧࠎ"))
                sys.exit(0)
            else:
                print(l1l_opy_ (u"ࠬࡈࡁࡅࠩࠏ"))
                sys.exit(1)
        elif l1l11_opy_ == l1l_opy_ (u"࠭ࡶࡦࡴ࡬ࡪࡾ࠭ࠐ") and len(l1ll_opy_) == 3:
            if verify(l1ll_opy_[2]):
                print(l1l_opy_ (u"ࠧࡐࡍࠪࠑ"))
                sys.exit(0)
            else:
                print(l1l_opy_ (u"ࠨࡄࡄࡈࠬࠒ"))
                sys.exit(1)
        elif l1l11_opy_ == l1l_opy_ (u"ࠩࡤࡧࡹ࡯ࡶࡢࡶࡨࠫࠓ") and len(l1ll_opy_) == 4:
            activate(l1ll_opy_[2], l1ll_opy_[3])
            sys.exit(0)
        elif l1l11_opy_ == l1l_opy_ (u"ࠪࡨࡪࡧࡣࡵ࡫ࡹࡥࡹ࡫ࠧࠔ") and len(l1ll_opy_) == 3:
            deactivate(l1ll_opy_[2])
            sys.exit(0)
        else:
            sys.exit(1)