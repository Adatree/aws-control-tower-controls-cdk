# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# List of Control Tower Guardrails
# https://docs.aws.amazon.com/controltower/latest/userguide/controltower-ug.pdf

# Organizational Unit Identifier

# The pattern for an organizational unit ID string requires "ou-" followed by
# from 4 to 32 lowercase letters or digits
# (the ID of the root that contains the OU).
# This string is followed by a second "-" dash and from 8 to 32
# additional lowercase letters or digits.


ACCOUNT_ID = "741634499280"
ROLE_ARN = "arn:aws:iam::741634499280:role/ControlTowerControlsCDK"
AWS_CONTROL_TOWER_REGION = "ap-southeast-2"
AWS_STACK_NAME="aws-control-tower-guardrails-workloads"

# pylint: disable=duplicate-code
GUARDRAILS_CONFIGURATION = [
    {
        "OrganizationalUnitIds": [
            "ou-cwi7-1q57z07v", # workloads-prod
            "ou-cwi7-yesweiwz", # workloads-nonprod
        ],
        "Enable-Control": {
            # Strongly recommended controls
            "AWS-GR_DETECT_CLOUDTRAIL_ENABLED_ON_MEMBER_ACCOUNTS",
            "AWS-GR_EBS_OPTIMIZED_INSTANCE",
            "AWS-GR_EC2_VOLUME_INUSE_CHECK",
            "AWS-GR_ENCRYPTED_VOLUMES",
            "AWS-GR_RDS_INSTANCE_PUBLIC_ACCESS_CHECK",
            "AWS-GR_RDS_SNAPSHOTS_PUBLIC_PROHIBITED",
            "AWS-GR_RDS_STORAGE_ENCRYPTED",
            "AWS-GR_RESTRICTED_COMMON_PORTS",
            "AWS-GR_RESTRICTED_SSH",
            "AWS-GR_RESTRICT_ROOT_USER",
            "AWS-GR_RESTRICT_ROOT_USER_ACCESS_KEYS",
            "AWS-GR_ROOT_ACCOUNT_MFA_ENABLED",
            "AWS-GR_S3_BUCKET_PUBLIC_READ_PROHIBITED",
            "AWS-GR_S3_BUCKET_PUBLIC_WRITE_PROHIBITED",
            
            # Elective Security Hub Standard
            "PKBECMZKORWL", # "SH.ACM.1",
            "PWJUGOAFXGNW", # "SH.APIGateway.1",
            "HCPQXEYLPUTG", # "SH.APIGateway.2",
            "PMGEOVFNRWUU", # "SH.APIGateway.3",
            "JDOSDYPYPULQ", # "SH.APIGateway.4",
            "QRFWQMUPBGAL", # "SH.APIGateway.5",
            "AOTXAAIXUZGO", # "SH.APIGateway.8",
            "XNMGCOKKDRTM", # "SH.APIGateway.9",
            "TDCHULZQJJYU", # "SH.Account.1",
            "HPBROJJRPRQP", # "SH.AutoScaling.1",
            "CFQPPPBKHPVE", # "SH.AutoScaling.2",
            "RSJYIFHSKNSS", # "SH.AutoScaling.3",
            "HCJSOXALINQW", # "SH.AutoScaling.4",
            "TNSLXHUTKWTZ", # "SH.AutoScaling.6",
            "XFPEFWDNOLGH", # "SH.AutoScaling.9",
            "BRQEJBSGCNRN", # "SH.Autoscaling.5",
            "JOVYOCPUBVQT", # "SH.CloudTrail.1",
            "RHDAYMWQSNQM", # "SH.CloudTrail.2",
            "RCLUACHBLUEJ", # "SH.CloudTrail.4",
            "WRJBVWCCGCPA", # "SH.CloudTrail.5",
            "OGBNWMEGMMNM", # "SH.CodeBuild.1",
            "NENDYNYMGBAL", # "SH.CodeBuild.2",
            "HBOJXAIXDHPV", # "SH.CodeBuild.3",
            "NQSLJQHQTLKU", # "SH.CodeBuild.4",
            "CLWTRMGVZRRH", # "SH.CodeBuild.5",
            "DHOJQSKCRIQH", # "SH.DMS.1",
            "ZZTZVYPQVDAK", # "SH.DynamoDB.1",
            "SCPPKINQMZAF", # "SH.DynamoDB.2",
            "QNCIIGXDITVK", # "SH.EC2.1",
            "CMHFRDIISEAB", # "SH.EC2.10",
            "VSUCLWGVQLDF", # "SH.EC2.15",
            "EVNHPWACQHEA", # "SH.EC2.16",
            "LWYOJLPCBZPK", # "SH.EC2.17",
            "UPVTHTZVSLWE", # "SH.EC2.18",
            "SQJOUZGFKZPV", # "SH.EC2.19",
            "RDJYZGXFHYUE", # "SH.EC2.2",
            "XSSLFGGJDHRI", # "SH.EC2.20",
            "YLOHXVLEFUBG", # "SH.EC2.21",
            "AJFFKKXRAFMB", # "SH.EC2.22",
            "QRHEHTVORUEM", # "SH.EC2.25",
            "QJPYFHYYTIDF", # "SH.EC2.3",
            "TWWDQASEKNOR", # "SH.EC2.4",
            "NZTMIPSZHEMV", # "SH.EC2.6",
            "KOPZMCROGHHM", # "SH.EC2.7",
            "JIQJXDPKNWCG", # "SH.EC2.8",
            "MQLRBDKQRBRZ", # "SH.EC2.9",
            "KTMZOOLGTWJX", # "SH.ECR.1",
            "THACMOMUCYAC", # "SH.ECR.2",
            "VMXVKJDQHDKB", # "SH.ECR.3",
            "CPDDHHPDKPIP", # "SH.ECS.1",
            "WILNHTOPFEWQ", # "SH.ECS.10",
            "MGJPDOBPUTIT", # "SH.ECS.12",
            "OAVLGBTROIFK", # "SH.ECS.2",
            "XTGMIDMJOWXW", # "SH.ECS.3",
            "LFUVYWFYYLLU", # "SH.ECS.4",
            "XWHFZMHURMPA", # "SH.ECS.5",
            "HLGKEXFGGOBE", # "SH.ECS.8",
            "TTLLYUNPAEQS", # "SH.EFS.1",
            "OJAGQJKAXRQT", # "SH.EFS.2",
            "OPPEWLVDKCXA", # "SH.EFS.3",
            "UWYRRBPEEWVO", # "SH.EFS.4",
            "DAMQGUZZUZBH", # "SH.EKS.2",
            "ZDVYGBSRJWYG", # "SH.ELB.10",
            "UXUMUBGBZHZO", # "SH.ELB.12",
            "ZUSLMMQOYOHO", # "SH.ELB.13",
            "NTKIROXXRLDD", # "SH.ELB.14",
            "HQUTVBZCPUEL", # "SH.ELB.2",
            "WLNVBASSPYBO", # "SH.ELB.3",
            "FIPLHETXVCED", # "SH.ELB.4",
            "HPXOCKUZZONE", # "SH.ELB.5",
            "PJAZYXFFMUVW", # "SH.ELB.6",
            "LPNJZVNGKYJN", # "SH.ELB.7",
            "LBDQCQLATJBB", # "SH.ELB.8",
            "PYRVSCBYFIYM", # "SH.ELB.9",
            "FJVEBRUCXPRO", # "SH.ELBv2.1",
            "GJCORWHPFGQY", # "SH.EMR.1",
            "SFSPFDZNCYNL", # "SH.ES.1",
            "BAQAAMCLMWUE", # "SH.ES.2",
            "LDLVCUOJCZXV", # "SH.ES.3",
            "NTWHSOQIKOPQ", # "SH.ES.4",
            "HBJICLMPQAQO", # "SH.ES.5",
            "LSVJLTKRGRNL", # "SH.ES.6",
            "YKZLIAMKUETJ", # "SH.ES.7",
            "CHITVXZCWFAK", # "SH.ES.8",
            "IVNFFJMNHDXC", # "SH.ElasticBeanstalk.1",
            "ALIABGGIBJQX", # "SH.ElasticBeanstalk.2",
            "SEPYALESYFHN", # "SH.GuardDuty.1",
            "LFXQGUJOZIVJ", # "SH.IAM.1",
            "YKNIXGERUKGE", # "SH.IAM.2",
            "CWYTGQUDYNSL", # "SH.IAM.21",
            "ZWZXSXOWDRJN", # "SH.IAM.3",
            "CVTOQOHCXJYE", # "SH.IAM.4",
            "PLGJLSNGGCIG", # "SH.IAM.5",
            "DJMVZWKQLOWP", # "SH.IAM.6",
            "XLUHJBTPSEGR", # "SH.IAM.7",
            "HEXKEUELTWUJ", # "SH.IAM.8",
            "YBJERSBVCEHS", # "SH.KMS.1",
            "NHKYZBGUEQPJ", # "SH.KMS.2",
            "BDIQMPNVEKNT", # "SH.KMS.3",
            "LJRFKNWNZTFU", # "SH.Kinesis.1",
            "UQXXELUQDDBO", # "SH.Lambda.1",
            "TOCWOWCANSFU", # "SH.Lambda.2",
            "WTXQRFALXGYL", # "SH.Lambda.5",
            "TIPAEJGHISPE", # "SH.NetworkFirewall.3",
            "EVSNHFCDZNEP", # "SH.NetworkFirewall.4",
            "VZMVHIMBIXOW", # "SH.NetworkFirewall.5",
            "MMCBTWVVBBFM", # "SH.NetworkFirewall.6",
            "GNNUAYUHJXLT", # "SH.Opensearch.1",
            "QWJLMXTGTTTY", # "SH.Opensearch.2",
            "QPRZHOWCOFOW", # "SH.Opensearch.3",
            "YGRKTWGZGYWP", # "SH.Opensearch.4",
            "OZIJZGYJIAUK", # "SH.Opensearch.5",
            "FTZIOOVBEHSU", # "SH.Opensearch.6",
            "EGTEXCKXTWYU", # "SH.Opensearch.7",
            "MQGZXOCEDKKX", # "SH.Opensearch.8",
            "KMPUUHKSUHBG", # "SH.RDS.1",
            "SMAVVTOYNJTI", # "SH.RDS.10",
            "PVJEIOWFEXGW", # "SH.RDS.11",
            "SFKATYNUSZRY", # "SH.RDS.13",
            "SRFNCNDSXZNT", # "SH.RDS.17",
            "RBYPDKTCHCVN", # "SH.RDS.18",
            "FDBSHSSUIULV", # "SH.RDS.19",
            "IWPFNXTZXADU", # "SH.RDS.2",
            "SIZRZVALISEG", # "SH.RDS.20",
            "BEAJMSHPLZAF", # "SH.RDS.21",
            "HGUANBQWZZZT", # "SH.RDS.22",
            "ZRQKSDQFNGQJ", # "SH.RDS.23",
            "BGPIYTQZCFXL", # "SH.RDS.25",
            "OKWMNXYZRUVG", # "SH.RDS.3",
            "UOCQAVOKOBTP", # "SH.RDS.4",
            "IRSIBRZRNPGJ", # "SH.RDS.5",
            "LJQFIHVOJEWC", # "SH.RDS.6",
            "CDKCDVDPAZJE", # "SH.RDS.8",
            "FPPDNGIQPZQT", # "SH.RDS.9",
            "WVIYUKDGFONY", # "SH.Redshift.1",
            "LQIBXYSZTOTD", # "SH.Redshift.10",
            "ORJWWXAPJACW", # "SH.Redshift.2",
            "UNNOEVFPFBMC", # "SH.Redshift.4",
            "WMXBZOHRKUOQ", # "SH.Redshift.6",
            "MVNWOYAUMTGJ", # "SH.Redshift.7",
            "XIDWPGTUKALT", # "SH.Redshift.8",
            "TTPOHLOSZBPO", # "SH.Redshift.9",
            "UBQSERAFQQLI", # "SH.S3.1",
            "OEWTPHSMPPGY", # "SH.S3.10",
            "HYDZJVQVOSSG", # "SH.S3.11",
            "IYZUNEUFKEBY", # "SH.S3.12",
            "TWWHDSTFPQWH", # "SH.S3.13",
            "WUHZWRYEJOUJ", # "SH.S3.2",
            "YJQGDKELZCKA", # "SH.S3.3",
            "MYWMNVQHDBPC", # "SH.S3.5",
            "FGNEAZJPHZUU", # "SH.S3.6",
            "HISIOKDAAMQR", # "SH.S3.8",
            "ZPOEOPATKJIC", # "SH.S3.9",
            "RJPBPBVBLXQI", # "SH.SNS.1",
            "YVTYTAYMHBIH", # "SH.SNS.2",
            "ENSHCNPLXZHX", # "SH.SQS.1",
            "RLRUQAVPCAZI", # "SH.SSM.1",
            "LARTAAZXHQGH", # "SH.SSM.2",
            "SFESCRTZJFXB", # "SH.SSM.3",
            "RKBCVEOAAXFA", # "SH.SSM.4",
            "LYBVPJQFKFUM", # "SH.SageMaker.1",
            "XWKDVYDAVXSW", # "SH.SageMaker.2",
            "GHYJJWOGIPDS", # "SH.SageMaker.3",
            "PIPRTUKNSOCX", # "SH.SecretsManager.1",
            "HOQMRBMNIKAW", # "SH.SecretsManager.2",
            "FNKXYQSZMWQM", # "SH.SecretsManager.3",
            "PTCINVDOZREK", # "SH.SecretsManager.4",
            "ZMFZRNVVUDDS", # "SH.WAF.10",
            "YJAUIVTCYRJW", # "SH.WAF.2",
            "CYGNEESCWZXG", # "SH.WAF.3",
            "LYLUSATWXWGZ", # "SH.WAF.4",

            # # # Elective Control Tower
            "OTJFGEEQXKHE", # "CT.ACM.PR.1",
            "MGCUKHLRUHGP", # "CT.APIGATEWAY.PR.1",
            "EAPHSJQRHZUB", # "CT.APIGATEWAY.PR.2",
            "NGDIEPXBGZNX", # "CT.APIGATEWAY.PR.3",
            "WUQUVNLUXDQU", # "CT.APIGATEWAY.PR.4",
            "RBLHXKSFLKZA", # "CT.APIGATEWAY.PR.5",
            # "VZIWINLZXVMA", # "CT.APPSYNC.PR.1",
            # "GUKAWPWOAMGJ", # "CT.AUTOSCALING.PR.1",
            # "FWWWWDZRSYOB", # "CT.AUTOSCALING.PR.2",
            # "PDKMRLRUFNDY", # "CT.AUTOSCALING.PR.3",
            # "DIXWASPFNOFQ", # "CT.AUTOSCALING.PR.4",
            # "AQIXLPCCRQHS", # "CT.AUTOSCALING.PR.5",
            # "HYEMAFKYGEOG", # "CT.AUTOSCALING.PR.6",
            # "ZBBMSBCWHDJT", # "CT.AUTOSCALING.PR.8",
            # "UHAFTVUQLBJQ", # "CT.CLOUDFORMATION.PR.1",
            "HGEUZPXSVDOS", # "CT.CLOUDFRONT.PR.1",
            "XSFJGHXKKXJQ", # "CT.CLOUDFRONT.PR.10",
            "OLKKBIYGTTTV", # "CT.CLOUDFRONT.PR.11",
            "NMGEPJROACOH", # "CT.CLOUDFRONT.PR.2",
            "MCQETJVLFUOU", # "CT.CLOUDFRONT.PR.3",
            "ELYJMXPJVKEI", # "CT.CLOUDFRONT.PR.4",
            "COFQNFPVILDJ", # "CT.CLOUDFRONT.PR.5",
            "IYBPCXPFECFI", # "CT.CLOUDFRONT.PR.6",
            "AQDUDHILVQNE", # "CT.CLOUDFRONT.PR.7",
            "FWXCSWFYXMCI", # "CT.CLOUDFRONT.PR.8",
            "MRNNWKOBUPWW", # "CT.CLOUDFRONT.PR.9",
            "MQTVMQFRAQQV", # "CT.CLOUDTRAIL.PR.1",
            "DTIKKBFJWTRD", # "CT.CLOUDTRAIL.PR.2",
            "AKRKBPXLHCRO", # "CT.CLOUDTRAIL.PR.3",
            "MOWBJMXOIHSB", # "CT.CLOUDWATCH.PR.1",
            "HEBNGALBPYXJ", # "CT.CLOUDWATCH.PR.2",
            "YHKYBCWCRLJJ", # "CT.CLOUDWATCH.PR.3",
            "CLDCBWOSIAUL", # "CT.CLOUDWATCH.PR.4",
            # "SCDVMCSBZZBP", # "CT.CODEBUILD.PR.1",
            # "CDUPZGSWHYDK", # "CT.CODEBUILD.PR.2",
            # "QYCIHTAXYLTZ", # "CT.CODEBUILD.PR.3",
            # "XWXSPGHBLRFI", # "CT.CODEBUILD.PR.4",
            # "YKADOBILMOXE", # "CT.CODEBUILD.PR.5",
            # "BKDGPCXEHUYM", # "CT.CODEBUILD.PR.6",
            # "WQDLGHQPLUEZ", # "CT.DAX.PR.1",
            # "ZERDIGHMXMHK", # "CT.DMS.PR.1",
            # "LVZGOWHNFFQQ", # "CT.DOCUMENTDB.PR.1",
            # "YDRKNNEUEWMB", # "CT.DOCUMENTDB.PR.2",
            "HYEXGEAODQCG", # "CT.DYNAMODB.PR.1",
            "MXJNGHQYSQWT", # "CT.DYNAMODB.PR.2",
            # "IZBFOJRZKBEV", # "CT.EC2.PR.1",
            # "PBNLHCFGRZZO", # "CT.EC2.PR.10",
            # "HNTCZVIEEJOI", # "CT.EC2.PR.11",
            # "DRPWGXJHMIQA", # "CT.EC2.PR.12",
            # "OSVHEFPIYSYR", # "CT.EC2.PR.13",
            # "TPIXAIIDPGBY", # "CT.EC2.PR.2",
            # "WUNOAUPAPJBR", # "CT.EC2.PR.3",
            # "GEQABOPVFXCO", # "CT.EC2.PR.4",
            # "JSPEJFTHBYZF", # "CT.EC2.PR.5",
            # "NCDDQQZLDCZI", # "CT.EC2.PR.6",
            # "QVYBWOWBJXKC", # "CT.EC2.PR.7",
            # "WTYIJXIQQBWX", # "CT.EC2.PR.8",
            # "NKVJXXQBVISF", # "CT.EC2.PR.9",
            # "QBVJWKFJGIXU", # "CT.ECR.PR.1",
            # "QZCGKPXCBXGB", # "CT.ECR.PR.2",
            # "NEMIRSQYEPIE", # "CT.ECR.PR.3",
            # "AELENOQZMXVF", # "CT.ECS.PR.1",
            # "BARUWERYCVPZ", # "CT.ECS.PR.10",
            # "EUFKWMGWEVVF", # "CT.ECS.PR.11",
            # "QANDDOVBOKJX", # "CT.ECS.PR.12",
            # "WXYOROQYZPPG", # "CT.ECS.PR.2",
            # "LHNFHNNMMIXX", # "CT.ECS.PR.3",
            # "NRNXSUVDQAOK", # "CT.ECS.PR.4",
            # "OOZUIEFUETGL", # "CT.ECS.PR.5",
            # "ALOSYSCTDXMC", # "CT.ECS.PR.6",
            # "NEZKAVUMHCLM", # "CT.ECS.PR.7",
            # "VAHLXFOOZHSE", # "CT.ECS.PR.8",
            # "YXLNPXSEMFTR", # "CT.ECS.PR.9",
            # "NJSROBYVJRTO", # "CT.EKS.PR.1",
            # "PGZSVHJPXLRN", # "CT.ELASTICACHE.PR.1",
            # "TIWUDRZWGRHU", # "CT.ELASTICACHE.PR.2",
            # "BPLCSUSNIIYE", # "CT.ELASTICACHE.PR.3",
            # "AYHVEAYSGMHD", # "CT.ELASTICACHE.PR.4",
            # "ZHSLHILXVOCO", # "CT.ELASTICACHE.PR.5",
            # "WBJIXMOKJKNB", # "CT.ELASTICACHE.PR.6",
            # "HBXNCBGUQCBZ", # "CT.ELASTICACHE.PR.7",
            # "YHIWFCYQDARH", # "CT.ELASTICBEANSTALK.PR.1",
            # "UOCTRMADKUPW", # "CT.ELASTICBEANSTALK.PR.2",
            # "XPBHHEZZNQJS", # "CT.ELASTICBEANSTALK.PR.3",
            # "QECOJWZQHMJQ", # "CT.ELASTICFILESYSYSTEM.PR.1",
            # "VXMYEULBUKRK", # "CT.ELASTICFILESYSYSTEM.PR.2",
            # "FINCEVUKQTHU", # "CT.ELASTICFILESYSYSTEM.PR.3",
            # "THCBRFJBEVKS", # "CT.ELASTICFILESYSYSTEM.PR.4",
            "JWBLMBPMKKDD", # "CT.ELASTICLOADBALANCING.PR.1",
            "BARRVADARLXA", # "CT.ELASTICLOADBALANCING.PR.10",
            "RFHZPJREXLSE", # "CT.ELASTICLOADBALANCING.PR.11",
            "OLUIOTBVOOCS", # "CT.ELASTICLOADBALANCING.PR.12",
            "VDPRZIODKYSS", # "CT.ELASTICLOADBALANCING.PR.13",
            "OPRFIUYZWTCD", # "CT.ELASTICLOADBALANCING.PR.2",
            "DTFRJDGWCDVJ", # "CT.ELASTICLOADBALANCING.PR.3",
            "REBMKCJKOTPA", # "CT.ELASTICLOADBALANCING.PR.4",
            "RNHSNSUAJPAV", # "CT.ELASTICLOADBALANCING.PR.5",
            "TGXQXNZCCEXR", # "CT.ELASTICLOADBALANCING.PR.6",
            "FSRKKRIKNTVD", # "CT.ELASTICLOADBALANCING.PR.7",
            "NHXVNOSXDCMQ", # "CT.ELASTICLOADBALANCING.PR.8",
            "XCEABSKXHNEW", # "CT.ELASTICLOADBALANCING.PR.9",
            "CELIJOZUYTCC", # "CT.GUARDDUTY.PR.1",
            "OHTNYZERSTJL", # "CT.IAM.PR.1",
            "CAOCWBICFGOB", # "CT.IAM.PR.2",
            "DIYAWISHCSUP", # "CT.IAM.PR.3",
            "NIQNDDIAPPYT", # "CT.IAM.PR.4",
            # "PSTEFAEBICWJ", # "CT.IAM.PR.5",
            # "KREYISSWDIIL", # "CT.KINESIS.PR.1",
            "KZDJWGKCNWVI", # "CT.KMS.PR.1",
            "BAGTSQZJEERJ", # "CT.LAMBDA.PR.2",
            "ORTKUZLIVKOW", # "CT.LAMBDA.PR.3",
            # "ZBNZCKKEFZPZ", # "CT.NEPTUNE.PR.1",
            # "EPHJMXQEYSVC", # "CT.NEPTUNE.PR.2",
            # "GQZRECITMLZC", # "CT.NEPTUNE.PR.3",
            # "ITJWVPIYBVEB", # "CT.NETWORK-FIREWALL.PR.1",
            # "JTCRHWTVYTMB", # "CT.NETWORK-FIREWALL.PR.2",
            # "JFLLDLXJUPDD", # "CT.NETWORK-FIREWALL.PR.3",
            # "BOZPZUYFXHUQ", # "CT.NETWORK-FIREWALL.PR.4",
            # "ZKCZQKAZSTAI", # "CT.OPENSEARCH.PR.1",
            # "JUUVIFSWJWIT", # "CT.OPENSEARCH.PR.10",
            # "YBEBQCIZYYLW", # "CT.OPENSEARCH.PR.11",
            # "GIVZCHZYHVFF", # "CT.OPENSEARCH.PR.12",
            # "LIQKLRNJWVLN", # "CT.OPENSEARCH.PR.13",
            # "HYENHQKNDJCT", # "CT.OPENSEARCH.PR.14",
            # "GTQNOHLWVMVH", # "CT.OPENSEARCH.PR.15",
            # "SUIONSKYSCOB", # "CT.OPENSEARCH.PR.16",
            # "GYGEIIYYZNLM", # "CT.OPENSEARCH.PR.2",
            # "QQBYBBDRDPJS", # "CT.OPENSEARCH.PR.3",
            # "UYAXZWGNSLOM", # "CT.OPENSEARCH.PR.4",
            # "ORIKZBBNSZRB", # "CT.OPENSEARCH.PR.5",
            # "UTDGLWWSQDEU", # "CT.OPENSEARCH.PR.6",
            # "BEKZJRWESGED", # "CT.OPENSEARCH.PR.7",
            # "RUFEVUMSOQXR", # "CT.OPENSEARCH.PR.8",
            # "GLPWOLQVEQJQ", # "CT.OPENSEARCH.PR.9",
            # "XFYDDJQMPBSV", # "CT.RDS.PR.1",
            # "OVTFQMGWPNHM", # "CT.RDS.PR.10",
            # "OXXJQNOBPMSW", # "CT.RDS.PR.11",
            # "VQTXJCSDCVNL", # "CT.RDS.PR.12",
            # "CWTDAVDXUYNS", # "CT.RDS.PR.13",
            # "HSIZECNPMUMR", # "CT.RDS.PR.14",
            # "RZHJAVYJQGUI", # "CT.RDS.PR.15",
            # "JCCMUPZAXMMW", # "CT.RDS.PR.16",
            # "TKAIVNUOZEOP", # "CT.RDS.PR.17",
            # "TXDOPOOEFOGJ", # "CT.RDS.PR.18",
            # "AKURSKMXIRNZ", # "CT.RDS.PR.19",
            # "LNDHGBLTEXAL", # "CT.RDS.PR.2",
            # "RKTXRGUXFWXY", # "CT.RDS.PR.20",
            # "GOGYCLISXJIE", # "CT.RDS.PR.21",
            # "SIJETKICNYSA", # "CT.RDS.PR.22",
            # "ODZTKLOPEVYA", # "CT.RDS.PR.23",
            # "UGDACEBUCTME", # "CT.RDS.PR.24",
            # "BLFCABKJKCSA", # "CT.RDS.PR.25",
            # "KGVGCJNUMNIY", # "CT.RDS.PR.3",
            # "VGJJUWDNFDIK", # "CT.RDS.PR.4",
            # "VTWUXLYFANSP", # "CT.RDS.PR.5",
            # "MKNYWNVXKUKG", # "CT.RDS.PR.6",
            # "BVMANNHHVIJJ", # "CT.RDS.PR.7",
            # "GJKUHDAQKCNH", # "CT.RDS.PR.8",
            # "TBPEWWYHECGP", # "CT.RDS.PR.9",
            # "QUVPAAZPCFDZ", # "CT.REDSHIFT.PR.1",
            # "CMTVPJTIHQTJ", # "CT.REDSHIFT.PR.2",
            # "TZMQFTLFIYII", # "CT.REDSHIFT.PR.3",
            # "DJJVYZTHHNQU", # "CT.REDSHIFT.PR.4",
            # "ICXWYEEBLZWH", # "CT.REDSHIFT.PR.5",
            # "KCSAGKLDYNMB", # "CT.REDSHIFT.PR.6",
            # "IJMLIAVPGIOI", # "CT.REDSHIFT.PR.7",
            # "KLGGBJEKOFDX", # "CT.REDSHIFT.PR.8",
            "WRGFYNFNMLEH", # "CT.S3.PR.1",
            # "XUAWJGYLSKOU", # "CT.S3.PR.10",
            # "EUTFKNVDBWID", # "CT.S3.PR.11",
            "MSRDMFGAVCXV", # "CT.S3.PR.2",
            "RRBBSRTVOULJ", # "CT.S3.PR.3",
            # "TJVPIRLFQNJU", # "CT.S3.PR.4",
            # "XBIANCENZNPT", # "CT.S3.PR.5",
            # "WVHLLZEVRMCQ", # "CT.S3.PR.6",
            # "BYKXCKKRYVIV", # "CT.S3.PR.8",
            # "MOCNFRGVJQIQ", # "CT.S3.PR.9",
            # "KJAHYCKSSRAA", # "CT.SAGEMAKER.PR.1",
            # "WHZCFXEMTXVF", # "CT.SAGEMAKER.PR.2",
            # "WFSJGEHTGUJD", # "CT.SAGEMAKER.PR.3",
            "RBKKATWLGQVS", # "CT.SQS.PR.1",
            "NWPVCUCMYWJV", # "CT.SQS.PR.2",
            # "HYFUIUJOXQNV", # "CT.STEPFUNCTIONS.PR.1",
            # "BUACWBSQOPNW", # "CT.STEPFUNCTIONS.PR.2",
            # "JGWGMJBHDRUF", # "CT.WAF-REGIONAL.PR.1",
            # "QWRJQUNFEALJ", # "CT.WAF-REGIONAL.PR.2",
            # "LBEBQHSFDADD", # "CT.WAF.PR.1",
            # "ZWQCPIXANTTE", # "CT.WAF.PR.2",
            "ITRZPFPNHOVU", # "CT.WAFV2.PR.1",
            "HGYKZRUFIFSG", # "CT.WAFV2.PR.2",
        },
    }
]
