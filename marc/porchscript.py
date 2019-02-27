PorchFT = train['WoodDeckSF'] + train['OpenPorchSF'] + train['EnclosedPorch'] + train['3SsnPorch'] + train['ScreenPorch']
train['PorchYN'] = [0 if x==0 else 1 for x in PorchFT]  
train['RecSpaceFt'] = PorchFT + train['LowQualFinSF']
