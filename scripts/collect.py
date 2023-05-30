'''
This is a quick program using BioPython and SeqIO to take a folder of ffn files
read then in, build a dictionary, and return the sequence of a gene of interest.
This was written to work with the ffn files output by prokka, and will print
sequences and locus tags in fasta format to the terminal where they can be sorted
further
'''
import os
import sys
import Bio
from Bio import SeqIO

###List of key words that you want to search for in the genomes
#List1
up_1hpi = ["KK01_06750", "KK01_01150", "KK01_09685", "KK01_01155", "KK01_02635", "KK01_01800", "KK01_06060", "KK01_04545", "KK01_08930", "KK01_03425", "KK01_05310", "KK01_02915", "KK01_01145", "KK01_06065", "KK01_01600", "KK01_02260", "KK01_07765", "KK01_03075", "KK01_09350", "KK01_04650", "KK01_01210", "KK01_05315"]
down_1hpi = ["KK01_05775", "KK01_02170", "KK01_06775", "KK01_07180", "KK01_06810", "KK01_02080", "KK01_00410", "KK01_00395", "KK01_02270", "KK01_09225", "KK01_10065", "KK01_07270", "KK01_07580", "KK01_06280", "KK01_00400", "KK01_09645", "KK01_02085", "KK01_08880", "KK01_06035", "KK01_04865", "KK01_03510", "KK01_04590", "KK01_06285", "KK01_05490", "KK01_09210", "KK01_06405", "KK01_07530", "KK01_07540", "KK01_09215", "KK01_02350", "KK01_08830", "KK01_07445", "KK01_00405", "KK01_02805"]
up_8hpi = ["KK01_07900", "KK01_02980", "KK01_03125", "KK01_03180", "KK01_04300", "KK01_07895", "KK01_02810", "KK01_03175", "KK01_04545", "KK01_03085", "KK01_03240", "KK01_02790", "KK01_04315", "KK01_04640", "KK01_05065", "KK01_05060", "KK01_01800", "KK01_00415", "KK01_04285", "KK01_05485", "KK01_01355", "KK01_09075", "KK01_03185", "KK01_03075", "KK01_00775", "KK01_03450", "KK01_07765", "KK01_09660", "KK01_02490", "KK01_05045", "KK01_06525", "KK01_02795", "KK01_02420", "KK01_04245", "KK01_04280", "KK01_00020", "KK01_01145", "KK01_01765", "KK01_02515", "KK01_03190", "KK01_09665"]
down_8hpi = ["KK01_07855", "KK01_06955", "KK01_08330", "KK01_07180", "KK01_08795", "KK01_02075", "KK01_08610", "KK01_09345", "KK01_00400", "KK01_08790", "KK01_02005", "KK01_02170", "KK01_03760", "KK01_06075", "KK01_09265", "KK01_06950", "KK01_08800", "KK01_06910", "KK01_02085", "KK01_08605", "KK01_00230", "KK01_01550", "KK01_00200", "KK01_00210", "KK01_08515", "KK01_02080", "KK01_05325", "KK01_04025", "KK01_07195", "KK01_06805", "KK01_07200", "KK01_00445", "KK01_03750", "KK01_07175", "KK01_09225", "KK01_08525", "KK01_00990", "KK01_03545", "KK01_01220", "KK01_08620", "KK01_04610", "KK01_09210", "KK01_08880", "KK01_01840", "KK01_03740", "KK01_06810", "KK01_06175", "KK01_07580", "KK01_00690", "KK01_08600", "KK01_01050", "KK01_03510", "KK01_00805"]
up_14hpi = ["KK01_00290", "KK01_00805", "KK01_03125", "KK01_06750", "KK01_02980", "KK01_04250", "KK01_04340", "KK01_03415", "KK01_05520", "KK01_03410", "KK01_00120", "KK01_07900", "KK01_07895", "KK01_02790", "KK01_05290", "KK01_02805", "KK01_02985", "KK01_07360", "KK01_06860", "KK01_03580", "KK01_09280", "KK01_04570", "KK01_07595", "KK01_08280", "KK01_07355", "KK01_02355", "KK01_03885", "KK01_05280", "KK01_00220", "KK01_08405", "KK01_01235", "KK01_06135", "KK01_08410", "KK01_01645", "KK01_00285", "KK01_04900", "KK01_07125", "KK01_09075", "KK01_00415", "KK01_09490", "KK01_09415", "KK01_08555", "KK01_01100", "KK01_05070", "KK01_09070", "KK01_05900", "KK01_05420", "KK01_05275", "KK01_01115", "KK01_01990", "KK01_09685", "KK01_05415", "KK01_03455", "KK01_01335", "KK01_01950", "KK01_00755", "KK01_02265", "KK01_00905", "KK01_02775", "KK01_06485", "KK01_05605", "KK01_00430", "KK01_04640", "KK01_05890", "KK01_05895", "KK01_08580", "KK01_09465", "KK01_09240", "KK01_06690", "KK01_06480", "KK01_08500", "KK01_01355", "KK01_08945", "KK01_00325", "KK01_06580", "KK01_05060", "KK01_04720", "KK01_04245", "KK01_00575", "KK01_05600", "KK01_03735", "KK01_04220", "KK01_01330", "KK01_09115", "KK01_06475", "KK01_03570", "KK01_08415", "KK01_01505", "KK01_04715", "KK01_09885", "KK01_00095", "KK01_06490", "KK01_05045", "KK01_01765", "KK01_01205", "KK01_05490", "KK01_02625", "KK01_03665", "KK01_02545", "KK01_07600", "KK01_04065", "KK01_02515", "KK01_00525", "KK01_00840", "KK01_10045", "KK01_04460", "KK01_03450", "KK01_01210", "KK01_09680", "KK01_09665"]
down_14hpi = ["KK01_07050", "KK01_07645", "KK01_08550", "KK01_01515", "KK01_07025", "KK01_01760", "KK01_01520", "KK01_06565", "KK01_08645", "KK01_06785", "KK01_07100", "KK01_02310", "KK01_01525", "KK01_09965", "KK01_06790", "KK01_05810", "KK01_06570", "KK01_01550", "KK01_07005", "KK01_07030", "KK01_06925", "KK01_04670", "KK01_08610", "KK01_02005", "KK01_02005", "KK01_01755", "KK01_07480", "KK01_07000", "KK01_01105", "KK01_06970", "KK01_08790", "KK01_06080", "KK01_06980", "KK01_06930", "KK01_06985", "KK01_06995", "KK01_09345", "KK01_00155", "KK01_02320", "KK01_08330", "KK01_08795", "KK01_06940", "KK01_06955", "KK01_09150", "KK01_06935", "KK01_02915", "KK01_03295", "KK01_07405", "KK01_06975", "KK01_06460", "KK01_02080", "KK01_07035", "KK01_06960", "KK01_01855", "KK01_01570", "KK01_00200", "KK01_04165", "KK01_07415", "KK01_02170", "KK01_04035", "KK01_01550", "KK01_00235", "KK01_09265", "KK01_06075", "KK01_03050", "KK01_00240", "KK01_06920", "KK01_01225", "KK01_05795", "KK01_04170", "KK01_06025", "KK01_05305", "KK01_03880", "KK01_08605", "KK01_07015", "KK01_00225", "KK01_05530", "KK01_01865", "KK01_06950", "KK01_06990", "KK01_08800", "KK01_07330", "KK01_07395", "KK01_06015", "KK01_00685", "KK01_07010", "KK01_05800", "KK01_07410", "KK01_01985", "KK01_06805", "KK01_04940", "KK01_05445", "KK01_04025", "KK01_01220", "KK01_05585", "KK01_04180", "KK01_06965", "KK01_00990", "KK01_06065", "KK01_01680", "KK01_08515", "KK01_01695", "KK01_03870", "KK01_07800", "KK01_01745", "KK01_00230", "KK01_04030", "KK01_08075", "KK01_01305", "KK01_07175", "KK01_03775", "KK01_07580", "KK01_03865", "KK01_04930", "KK01_03545", "KK01_01690", "KK01_02050", "KK01_06010", "KK01_05805", "KK01_01545", "KK01_07240", "KK01_06180", "KK01_03620", "KK01_01860", "KK01_06405", "KK01_07445", "KK01_06175", "KK01_03420", "KK01_07580", "KK01_01615", "KK01_08525", "KK01_06910", "KK01_06810", "KK01_06885", "KK01_06060", "KK01_06880", "KK01_00165", "KK01_04610", "KK01_05325", "KK01_04475", "KK01_07200", "KK01_06285", "KK01_08685", "KK01_02430", "KK01_08620", "KK01_07195", "KK01_01750", "KK01_00850", "KK01_08600", "KK01_05320", "KK01_04120", "KK01_02910", "KK01_00690", "KK01_06905", "KK01_04440", "KK01_01840", "KK01_04865", "KK01_09215", "KK01_00960", "KK01_05495", "KK01_04175", "KK01_07660", "KK01_03875"]



###path to ffn file directory
#file = os.listdir("/Users/danielmorreale/Desktop/KK01_KK03_Genomes/KK01/bakta")

##read in each ffn file in the directory one at a time
#for item in file: REPLACE ALL_cat.ffn WITH PATH TO YOUR DIRECTIORY
with open("/Users/danielmorreale/Desktop/KK01_KK03_Genomes/KK01/bakta/KK01.faa", "rU") as handle:
    ###parse into a dictionary that has all data saved
    dict = SeqIO.index("/Users/danielmorreale/Desktop/KK01_KK03_Genomes/KK01/bakta/KK01.faa","fasta")
    for record in SeqIO.parse(handle, "fasta"):
        #for each keyword listed above, see if that is in any descriptions lines from the fasta
        # for name in up_1hpi:
        #     if name in record.description:
        #         ##collect fasta descriptions, append with the strain name
        #         gene = record.description
        #         #gene = gene + "_" + item
        #         ##collect fasta seq and print all to terminal
        #         seq = record.seq
        #         print (">1up_", gene, "\n", seq) 
        # for name in down_1hpi:
        #     if name in record.description:
        #         ##collect fasta descriptions, append with the strain name
        #         gene = record.description
        #         #gene = gene + "_" + item
        #         ##collect fasta seq and print all to terminal
        #         seq = record.seq
        #         print (">1down_", gene, "\n", seq)
        # for name in up_8hpi:
        #     if name in record.description:
        #         ##collect fasta descriptions, append with the strain name
        #         gene = record.description
        #         #gene = gene + "_" + item
        #         ##collect fasta seq and print all to terminal
        #         seq = record.seq
        #         print (">8up_", gene, "\n", seq)
        # for name in down_8hpi:
        #     if name in record.description:
        #         ##collect fasta descriptions, append with the strain name
        #         gene = record.description
        #         #gene = gene + "_" + item
        #         ##collect fasta seq and print all to terminal
        #         seq = record.seq
        #         print (">8down_", gene, "\n", seq)
        # for name in up_14hpi:
        #     if name in record.description:
        #         ##collect fasta descriptions, append with the strain name
        #         gene = record.description
        #         #gene = gene + "_" + item
        #         ##collect fasta seq and print all to terminal
        #         seq = record.seq
        #         print (">14up_", gene, "\n", seq)
        for name in down_14hpi:
            if name in record.description:
                ##collect fasta descriptions, append with the strain name
                gene = record.description
                #gene = gene + "_" + item
                ##collect fasta seq and print all to terminal
                seq = record.seq
                print (">14down_", gene, "\n", seq)
