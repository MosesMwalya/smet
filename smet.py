import streamlit as st
import math




st.title('Safaricom Marketing Effectiveness TOOL - SMET')
st.sidebar.image("logo.png")


rad1 = st.sidebar.radio("MAIN INVESTMENT OBJECTIVE",["Increase Revenue",
                                               "Create Awareness",
                                               "Stimulate Usage",
                                               "Brand stickiness"])

st.write("")

st.sidebar.header("S.M.E.T TOOLS")
side_button1 = st.sidebar.button(label="SIMULATOR")
side_button2 = st.sidebar.button("OPTIMIZER")
side_button3 = st.sidebar.button("ADVANCED OPTIMIZER")
 

#ONLY SIMULATOR IS FUNCTIONING
st.header("Target Customer Details") 
#st.write("Give more details about your target Customer")
col01, col02, col03 = st.columns(3)
main_seg = col01.radio("Broad Customer Category",["Consumer", "Business"])

if main_seg=="Consumer":
    segs = col02.multiselect("Consumer Segments ",["Teens", 
                                      "Prudent Young", 
                                      "Trendy", 
                                      "Focused Young", 
                                      "Settled", 
                                      "Builders", 
                                      "Aspirers", 
                                      "Achievers"])
if main_seg=="Business":
    segs = col02.multiselect("Business Segments",["MiniFesting", 
                                   "ManiFesting", 
                                   "Latent Giants", 
                                   "Advancing Giants"])

regs = col03.multiselect("Region",["Metro", 
                                   "Rift", 
                                   "MT", 
                                   "Coast", 
                                   "GW"])

st.header("Proposed Market Investment Decision")
st.write("Input proposed spends in '000' Kshs")
st.write("")
   
col1, col2, col3, col4 = st.columns(4)

st.write("")

#col1.write("Amounts in '000'Kshs")
x1 = col1.number_input("Billboard ", value=None, placeholder="Amount")
x2 = col1.number_input("Digital ", value=None, placeholder="Amount")
x3 = col1.number_input("Poster", value=None, placeholder="Amount")
x9 = col1.number_input("Other Comms ", value=None, placeholder="Amount")

#col2.write("Amounts in '000'Kshs")
x4 = col2.number_input("Press", value=None, placeholder="Amount")
x5 = col2.number_input("Radio ", value=None, placeholder="Amount")
x6 = col2.number_input("TV ", value=None, placeholder="Amount")
x7 = col2.number_input("Magazine ", value=None, placeholder="Amount")

#col3.write("Amounts in '000'Kshs")
x8 = col3.number_input("Other Media ", value=None, placeholder="Amount")
x10 = col3.number_input("Sales Activation ", value=None, placeholder="Amount")
x11 = col3.number_input("Sales Promotion ", value=None, placeholder="Amount")
x21 = col3.number_input("Brand Assets", value=None, placeholder="Amount")

#col4.write("Amounts '000'Kshs")
x22 = col4.number_input("Experiential", value=None, placeholder="Amount")
x23 = col4.number_input("Sponsorships ", value=None, placeholder="Amount")
x24 = col4.number_input("Donations ", value=None, placeholder="Amount")
x25 = col4.number_input("Public Relations ", value=None, placeholder="Amount")

#Calculations
col1.write("")
calc_button = col1.button("ESTIMATE RETURN")

if calc_button:
    
    prior_adstock = [4.102951420, 
                     0.043231096, 
                     0.129607497, 
                     4507.524064522, 
                     156.612486040, 
                     552.5736841152, 
                     0.001518216, 
                     487.675260547, 
                     0.002479488, 
                     0.066208233, 
                     0.040566323, 
                     0.047586827, 
                     1353.663579925, 
                     0.022671302, 
                     13.232201263,
                     48.880440900]

    beta = [0.379191, 
            0.399519, 
            0.398340, 
            0.271894, 
            0.549827, 
            0.077940, 
            0.000000, 
            0.457379, 
            0.426756, 
            0.000000, 
            0.151849, 
            0.528776, 
            0.396603, 
            0.549997, 
            0.532469, 
            0.510443]

    alpha = [0.534152, 
             0.233079, 
             0.445883, 
             0.990000, 
             0.763319, 
             0.990000, 
             0.963458, 
             0.846506, 
             0.088410, 
             0.990000, 
             0.225562, 
             0.234294, 
             0.990000,	
             0.214209, 
             0.545986, 
             0.744244]

    slope = [-37.906233816, 
             13524.673130885, 
             -78.530992826, 
             -0.006020493, 
             1.489888426, 
             -0.131453325, 
             -1.911508278,	
             0.111609222, 
             -62772.561708118, 
             94059.875691415, 
             -15676.740695600, 
             15320.823463671, 
             -0.002690520, 
             49693.459340481, 
             36.931206475, 
             49693.459340481]


    x1_tr = ((prior_adstock[0]*beta[0])+x1)**alpha[0]
    x2_tr = ((prior_adstock[1]*beta[1])+x2)**alpha[1]
    x3_tr = ((prior_adstock[2]*beta[2])+x3)**alpha[2]
    x4_tr = ((prior_adstock[3]*beta[3])+x4)**alpha[3]
    x5_tr = ((prior_adstock[4]*beta[4])+x5)**alpha[4]
    x6_tr = ((prior_adstock[5]*beta[5])+x6)**alpha[5]
    x7_tr = ((prior_adstock[6]*beta[6])+x7)**alpha[6]
    x8_tr = ((prior_adstock[7]*beta[7])+x8)**alpha[7]
    x9_tr = ((prior_adstock[8]*beta[8])+x9)**alpha[8]
    
    x10_tr = ((prior_adstock[9]*beta[9])+x10)**alpha[9]
    x11_tr = ((prior_adstock[10]*beta[10])+x11)**alpha[10]
    
    x21_tr = ((prior_adstock[11]*beta[11])+x21)**alpha[11]
    x22_tr = ((prior_adstock[12]*beta[12])+x22)**alpha[12]
    x23_tr = ((prior_adstock[13]*beta[13])+x23)**alpha[13]
    x24_tr = ((prior_adstock[14]*beta[14])+x24)**alpha[14]
    x25_tr = ((prior_adstock[15]*beta[15])+x25)**alpha[15]
    

    total_return = (
        13679252.3563623 + 
        (x1_tr * slope[0]) +
        (x2_tr * slope[1]) +
        (x3_tr * slope[2]) +
        (x4_tr * slope[3]) +
        (x5_tr * slope[4]) +
        (x6_tr * slope[5]) +
        (x7_tr * slope[6]) +
        (x8_tr * slope[7]) +
        (x9_tr * slope[8]) +
        
        (x10_tr * slope[9]) +
        (x11_tr * slope[10]) +
    
        (x21_tr * slope[11]) +
        (x22_tr * slope[12]) +
        (x23_tr * slope[13]) +
        (x24_tr * slope[14]) +
        (x25_tr * slope[15])
        )

    total_return_mill = total_return/1_000
    #col1.write("")
    col1.write("Amount in Million Kshs")
    col1.write(str(round(total_return_mill,3)))
    
  