Hexadecimal 0-9 + A-F

1 0 0 0 0 0 0 0 = 128 0 = 0 A=10 F=15 so 16 total combos 1-15 + 0 = 16

0 0 0 0 0 0 0 0 = 0

0 0 0 0 0 0 0 1 = 1 Break into to 4 digit brackets

0 0 0 0 | 0 0 0 0 = 0

0 0 0 0 | 0 0 0 F = 15

0 0 0 0 | 0 0 1 0 = 16

FF=255 16\*16 = 256 – 1

1 0 0 0 | 0 0 0 0 = 128

8 4 2 1 | 0 0 0 0

80 = 128

1 1 1 1 | 1 1 1 1 =256

15 | 15 15\*15=225

or F | F as such FF is 255

0 0 0 0 | 0 0 0 0 = 0

0 0 0 0 | 0 0 0 0 = 0 0F

1 1 1 0 | 1 0 1 0 CA = 202

14 | 10 DA = 218

DB 219 DC 220 DD 221 DE 222 DF 223

E 0 is 224

E | A EA = 234

EB+ 235

FA = 250

0 0 0 0 | 0 0 0 0 = 0

1 1 0 1 | 0 0 0 0

D / 13 |

1 1 1 0

8 + 4 + 0 + 1 = 13

8 + 4 + 2 + 0 = 14 or E

1 1 1 0 0 | 0 0 0 0

128 + 64 +32 +16 |+8 + 4 +2 + 1

1 + 1 + 1 + 0 + | 0 + 0 + 0 + 0

128 + 64 + 192 +32 = 224+ 224 + 0

E 0

16 is 0 0 0 1 0 0 0 0 is 10

Easist to convert Decimal to Binary then Binary to Hex

1 1 1 1 | 0 0 0 0 or F0

240 128 + 64 +32 + 16 + 8 +4 + 2 + 1

P Address decimal = 10.1.1.1

Binary 00001010 . 00000001. 00000001. 00000001.

Hex 0A:01:01:01

IP Address decimal = 224.1.2.3

Binary 128+64.192+32 . 224 + 00000001

Hex 1110|0000 . 0000|0001 . 0000|0010 . 0000|0011

E0:01:02:03

172.16.35.123/20 255.255.240.0

Subnet 172.16.0.0

First is 172.16.32.1

Last is 172.16.47.254

Broad is 172.16.47.255

172.16.197.232/23 197

255.255.254.0

FF FF | 1111|111\0 0000 0001 0000 0002

172.16. (1100 0101).(0000 0000)

8 + 8 +7 mean hosts binary is 1 0000 0000 33

1 0000 0001

1 1111 1110

1 1111 1111

192+5197

CIDR /26

8+8+8+2

10.199.199.199 255.255.255.192

10.199.199.199/26

10.199.199.(1100|0111) 199 00111110 32+16+8+4+2+0 48+12 60+192 152

10.199.199.192-

10.199.199.252

FF FF FF

128 64 32 16 192 +32 224+16 240 + 8 4 2 1 15

10.199.199.199/22

255.255.1100|0111.0000|0000 240 + 8 + 4 is 252

10.199.1100|011\00.0000|||

10.199.1100|01\11.1110|||

10.199.199.254

10.199.192.

10.199.192+4+1 is 197.0

10.199.197.0

10.199.252.254

10.199.1111|1111.1111|1110

10.10.10.10/21

(1111|1111). (1111|1111).( 1111|1\000).(0000|0000)

(1111|1111). (1111|1111).( 0000|1\111.254000).(0000|0000)

10.10.15.254

255.255.248.0

10.10.0000.0100.0000

10.10.8.0

10.10.8.1 – 10.10.15.254

Broadcast is 10.10.15.255

10.10.111100010.10.7.254

For /24 or 255.255.255.0 aka 8+8+8+0 or 24

First 24 binary digits are all 1’s \ remaining digits are all zeros to get subnet address x.x.x.0/24

First 24 binary digits are all 1’s \ remaining digits are all zeros except the final digit which is a 1

this is the first host in the subnet. X.X.X.0/24

First 24 binary digits are all 1’s \ remaining digits are all 1’s except the final digit which is a 0.

this is the last host in the subnet. X.X.X.254/24

Add 1 to last host to get broadcast id

**172.172.172/25**

172.172.172.1010|1100 0111|1100

160 | 12 160+12=172

172.172.172.1\000|0000 Subnet in Binary

172.172.172.1\000|0001 First Host in Binary

172.172.172.1\111|1110 Last Host in Binary

172.172.172.1\111|1111 Broadcast in Binary

As such a host in this subnet range **172.172.172.172/25**

Subnet: 172.172.172.128

Begins: 172.172.172.129

Ends: 172.172.172.254

Broadcast Address: 172.172.172.255

Subnet Mask of: 255.255.255.128

**192.168.1.130/27**

192.168.1.1000|0010

8.8.8 is 24 fist 3 of final octet is 11100000 111 is 128+64+32 of 192+32 is 224 this is subnet

192.168.1.. 100\0|0000 Subnet in Binary

192.168.1..100\0|0001 First Host in Binary

192.168.1..100\1|1110 Last Host in Binary 128+16+8+4+2 30+128 158

192.168.1..100\1|1111 Broadcast in Binary

As such a host in this subnet range **192.168.1.130/27**

Subnet: 192.168.1.128

Begins: 192.168.1.129

Ends: 192.168.1.158

Broadcast Address: 192.168.1.159

Subnet Mask of: 255.255.255.224