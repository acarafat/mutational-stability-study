# Enlist Mutation 
# Enlist all mutation in an alignment 

from Bio import SeqIO

def seqIn(fileName):
    seqs = []
    for record in SeqIO.parse(fileName, 'fasta'):
        seqs.append([record.description, str(record.seq)])
    return seqs

# This can't handle multiple insertion
def enlistMutation(ref_seq, seq):
    mutations = set()
    pos = 1
    for i in range(len(seq[1])):            
        if ref_seq[1][i] != '-':
            pos = i+1
        else: 
            pos = i-1
        if ref_seq[1][i] != seq[1][i]:
            if ref_seq[1][i] == '-':
                pass
                #mutations.add(str(ref_seq[1][i-1]+str(pos)+'ins'+seq[1][i]))
            elif seq[1][i] == '-':
                pass
                #mutations.add(str(ref_seq[1][i]+str(pos)+'del'))
            else:
                mutations.add(str(ref_seq[1][i]+'A'+str(pos)+seq[1][i]))
    return mutations
    
def prepareFoldXList(all_seqs, fileOut):
    raw = ''
    ref_seq = all_seqs[0]
    all_mutations = []
    for seq in all_seqs[1:]:
        a = enlistMutation(ref_seq, seq)
        if a not in all_mutations:
            all_mutations.append(a)
    try:
        all_mutations.remove(set([]))
    except:
        pass
    for i in all_mutations:
        raw += ','.join(i)+';'+'\n'
    return raw
            
if __name__ == '__main__':
    subs = seqIn('../type O _BD_VP1_AA.fas')
    mutants = prepareFoldXList(subs, 'fmdv_mutants.txt')
        
        
    