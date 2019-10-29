# Use python3 not python2
# The original is 30533 bytes. 
# It's the GNU Header repeated 4 times.
# The gzip version compressed file is 2872 bytes
# the lzma version of our compreesed codes 
# is 2840 bytes
# We use lzma to compress our math operations
# to uncompress the GNU Header with better
# results than gzip in this case by using 
# an lzma header to compress our codes.
# We are not compressing the file, instead
# we are compressing the pattern used for 
# XOR operations to rebuild the original file
# In no way can you uncompress the code
# to reproduce the original without using our
# math XOR operations.
# This is to prove that XOR operations have
# repetition on par with the original file 
# just by compressing the maths logic. 
# I used gzip as an example as it doesn't
# compress repetition as well as other compressors.


import lzma

# This code uncompresses the math required to rebuild a GNU licence that is repeated 4 times.

code='fd377a585a000004e6d6b4460200210116000000742fe5a3e077450ad55d0000953185805d1e19050eb115bdd0f560d3516fc2a4d1f9603d38f615e4012ce3d463f56b72f09dcfe8746a3c95e5d95ba427f711d2e70cebbdda888a340eb8acb2dfcff6381b49d185051e595a1aec163eaf70cab9b67d9f953d62d5f99b4757434dbf72dbf14e5ca7c1f786a2e245f7b8969bd8232b9f5c48b3a6ef37c33ab46d89c67ddc793c8b1c9bd62219ce9f0fe529d33776e714c707db01084a93a26d14bdd331f8e46000d7356c29ca8214691a605586a6e24d53488d4de3de87f0487ff372d0f3a8c292547d1337ae8d133072f855deb17d9534c1d1fa20e5d6f3eeb4a5bdae17f898f3c2669cbe564f0e21f94c063e88edfaa21a6c4552350771b789d7fea56c9d100f8feb513e578aabc70a813870eb17c3da76c8420480fdcd8fd1025cfb090629e1f455bd99c906c97b5dc40f9ce3d5b9fd6752f4090106ff64d24be55338ff33c7af686981b0cf8b29a9db092016d8f971feb8f4c7a28ecb7413c6dee182b76b85b9a2e2574fedce00fdb9f5795934cd0f12c9194c20b6181cbe56764dac2ebaa184f738dd4c640546bbcef1288119d105ff29d1caf90144b82b8d13430b0f7bc02b934b24edc0d1b9d39e6e68e9c4727787f713eeebf73bf7c14cc91ce3279e80fcb5d97869201f89bd689f32644f1ecc437126e741e0d255e0236b0ff044b8c8f19eaab2f8931e057e61253d781c8a895f19d3e4bfdca1480eb25ecf5fe0b9226ef5a9ec3bbc5daa2a632f8ec36e66b1fad219adb2b7e4fb3f94ae725b36c4a1d3df3dcccc3cda58c1d428b10d6db6e94dbb5925a5cb5f8684a4b8754f6995f379f4fb0e5bd85aab83c66dea1fe8fb8ae69fc275b06e1f5d325a0d6f8b910cb50fbb0cdfec39111f8d48a2bcb218f4c1831e12ef0ec2e436c63555b6ce710cd4fb9598bb2d66eb733456187394c97462be70e7dc48a94df8f0e61b84f6ca558034ef2ac021bef029f27b3ed75b1514fb9ca5072a02e759ff7a1ba4d916b6e77d72e5cb0a49fb9bf856f4a6df9e2f7ec16e92a4442e60a9838be2757bc54fc4ee7dc687cf11f7a3c410cf536fb20474bba282c74622a27d49013ed387f0e59fb1b9699d73a279bdb5d4716be8fbe062aa5bc330f901bb474836632bc3f8370f3c754578d4d107be8b31870c5914701300e7d62bb243ad46dc7786b9ded96e3e8a36aa2aaaf77f79683b9b1179d2e9e623eda2657563fab531b523dc54d74de6a27a90cc6c87aaab1c03ed9bb69586d198be4080a6ad88d485b33cfc3b203e853fcbe000265681efafe50262f1685ecbad4c0f9e8fca72f92a826a033623af98fa6b9fc4007b2f3b2ee1b2f608d95039b6e0608839c957569ba6120dcc5110c79e7f3fb474f70f9a92d505fdede096333a9c3173884b8488ac1b0c12f57a2db90ecb1639c90004e5d59e3f5e0b45d6a29606f06622047e56b40ee8c959766fbd633b4d8549b75cb287af9515facebb6f4a57a1d6cebcb2ffbe7ae999e5d109096c0777034f5b7ea96b92e75e03457c0618785f2e0091d1e44be7ed7142e988e9694fbf81892c3cc1c7670900396d3a8bdef2494fcef9afe623b94a0d067354da3a4377fadd1e72480a55184bb182b2569b9dfa7c5d59c1d72c93b4e39d2e3055d3670a74669f02b2814d9608ae888dfe9707b1461f195d1e85a87a1eb4b5228a37ec1990ffa54f310f9732cfb789582304654d2f97c596d77d812cd42797992b6d87f395f8bb23235e1af668e72bb1a5d4668e7e59672aba817446379a3cabe3797ac1abcc7dad53b22d4ea4a3c71a491d88bd49e7c472b5e20f149c5ab69708bee8149c2583f93334e54132e18711fb3f59f8df1f4f5671ce0dcb54b8b45d9ef5097dd8630115b4f44352aefd73ca8a051536bdb4fcfdfaf1062e16d6c92266a056951d7799bea9b46d79a0c602fb3136450ba9e1a2a4a09490f388d3ffab52a22e66f82d106a91412f10a283a697eac2a7c3c0bb31ace9d1202c3d716d7ab666669d4880b72c7724faff0ccdf6908e48914f4642dfb6f9732cc2cf5331333e59e8f60d861dc531f846e4ae2f6944d523f5d06ab444d45b55f3d9771a1f395b9ba0edb93f868cdb2f15c3e7cb662fe6e62c76843afb329c517676a82b3d5e644df8671f5aa0478372125b6cb8648c34393186582eba5fd62984144d35ba074046fd52a187ef17a5915c2a5cbf90816678bfaff5bf21d2398c72e8183b4ed5c327010adbe0a6ef20f2938f5ac118b5f0f65ea32c40e73384d7dae11b816bbcfbacbb1db75cbef17c43333917067245232a9efa6984c612c7e415c71a5aa7109b5674eec99f07164ceba3b8cbf8fdfadf324b5acf89811aef310308588447442a083a8eea2bb7060e89ab438c4f76178947d9ede21fd2ab327d56c2d6705d41162d8795c1d55146f0bdc9e901981a04cbd8dce76037d9ec27318fe087b73bd0b4b8995513d950ee5cf1691b1c921fcbe69ef951d465bfc91fbd403b4ddb8b228507abdd09fb68cb0d9d1f327dfd3cbcab9e6a72b913d1c49c53f26c09fedd64e86c7c5715cd6820c034690cce9a96a96711556e7573439acd3361c40ebba90d98ebb7286ba1d58fa7bd9eaad3b1b670dd3369ddc719a1b39ef292ccd94fb46e4c674d88e262c597b4bbe201741f334130ba00cd4993c75bf3db75e8e3c703d8d1116f389f1152798ea49eabb3b12b808a238f2722968f28b779d9e5cde734425023c7bdb6d8eb8fc530261da60129bde2fb8c162831648e4ac169a845eec29d3610a5c5f2a62c088e84bb205b484326cc7cd0b0be5de6d4a0587ac00722aafcfe40b16c5f6a062cdd9fe23ec1d413c94fabd3894b5b9dac0e21ca12f25bc767b22724e9cd6499d8fde8aaa20ef6a15af813b3a713df3ee4d8c7f447e625a8af9950a3e8ebcc1139f8ef03c5fe003e5d7ed89096527771033ef945822cf625f703a7f25bb42f492eae542ebd1ec779854189df226d254fd93ee71183cbc3c0e9fc0676e3c6df363a783f3f3eff3d34586728d663334d4347180436c201daf2dfa307dd94a3b66d650c215341a590e77489c8e61439e6d9932b64fbe8292e57ef859204caa4ea5cc477fddefa4eed652c2f587b2909be2d306c176f0a263865b7ded7dcc3e0029f3f990df4e81bd06a189855970886a203fb9c7396eeaf44478ec26c19e7b0592f772d46636422135a7f9df24c5199c1e92a525b90a7666aeed46c59dfb7680d3f0e49c9c1457a322d2d459399810b8de1b6c40c12e64fd679bb58ad99b4329e5a5f45ce69fca80b9105cf857a1403952fbaf32daeb9750c88be3b749efe61b186f35170e72688a478b695319267452cdc4c4e668b53af2c23d5b5b29f3d7260b5a4524f3a9b6baa71c8f4cf7c95eb29050c3916c59d5686ff5919726402f06523674c3b8d1893d98a44154d0d240dd357e0bfd11c724ea9e02abf781230929e440084b94852e9db4fad27f4b8b6ddd5c92933d39470b4552cdb628f9710646289e271e7ab2946d0ae6c0a595178b6976b13dccc9e0c8040341b88a13787b93546139ac49b5a9b70eaae3a9311eb268f38bcbf3eba8284fffc19925c16ba00ff9bb8aeb095ef566c065d286b1bc81925df7e7f055706524047aaf084076bae5f2e9845acbe1085f708e07b220b54d12f2184001f6ad65a31978a9c95c71344dc4fde7bc1fa371d7d97677a8afd17bce479dc28dc81079719ae39fdf8325bee94721b8470981cff34b03457ca35619e146a032239e442dda0fb721a15241bacee5b4fc271ed4397e6ecd4d58ca20d0cc00af7ee4a5087f2c0f8b31926bbcb150e50f43de275d2b1fa8db8728f351e3be2860ddec9815007b918513420db484b6fc288ed00670e66db694e741a6a397ca9fe4e3b51e9913540ac5954fc8646f17fab5be98ea265478d00000000006102a54efb4c9eee0001f115c6ee0100a27bda5cb1c467fb020000000004595a'


def decompressmaplzma(code):
   return bin(int(lzma.decompress(bytes.fromhex(code)).hex(),16))[2:]

def decodethebetterstuff(themap):
  j=0
  y=1
  for c in range(1,len(themap)):
     if j < 0:
        if themap[c] == '0':
            j^=y
        else:
            j^=-y
     else:
        if themap[c] == '0':
            j^=-y
        else:
            j^=y
     y<<=1
  answer=((y>>1)-1)-(abs(j)>>1) 
  return answer


themap = decompressmaplzma(code)
origint = decodethebetterstuff(themap)
#print(bytes.fromhex(hex(origint)[2:]).decode())

zzwrite = open('gnu_repeat4.bin', 'wb')
zzbytes = bytes.fromhex(code)
zzwrite.write(zzbytes) 
zzwrite.close()

zzwrite = open('gnu_repeat4.txt', 'wb')
zzbytes = bytes.fromhex(hex(origint)[2:]) 
zzwrite.write(zzbytes) 
zzwrite.close() 

print("")
print("gnu_repeat4.txt and gnu_repeat4.bin has been created.")
