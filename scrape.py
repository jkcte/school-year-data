import pandas as pd

enrollmentCSV = 'ph_school_enrollment.csv'
strandCSV = 'ph_shs_table_strand.csv'

enrollment = pd.read_csv(enrollmentCSV)
strand = pd.read_csv(strandCSV)

# Group by the 'Region' column and sum the 'Grade 10' column
grade_11_ABM_per_region = enrollment.groupby('Region')['Grade 11 ABM'].sum()
grade_11_HUMSS_per_region = enrollment.groupby('Region')['Grade 11 HUMSS'].sum()
grade_11_STEM_per_region = enrollment.groupby('Region')['Grade 11 STEM'].sum()
grade_11_GAS_per_region = enrollment.groupby('Region')['Grade 11 GAS'].sum()
grade_11_TVL_per_region = enrollment.groupby('Region')['Grade 11 TVL'].sum()
grade_11_sports_per_region = enrollment.groupby('Region')['Grade 11 SPORTS'].sum()
grade_11_AnD_per_region = enrollment.groupby('Region')['Grade 11 A&D'].sum()
grade_11_maritime_per_region = enrollment.groupby('Region')['Grade 11 MARITIME'].sum()

# Combine all the strands into a single DataFrame
strands_per_region_11 = pd.DataFrame({
    'ABM': grade_11_ABM_per_region,
    'HUMSS': grade_11_HUMSS_per_region,
    'STEM': grade_11_STEM_per_region,
    'GAS': grade_11_GAS_per_region,
    'TVL': grade_11_TVL_per_region,
    'SPORTS': grade_11_sports_per_region,
    'A&D': grade_11_AnD_per_region,
    'MARITIME': grade_11_maritime_per_region
})

# Group by the 'Region' column and sum the 'Grade 12' column
grade_12_ABM_per_region = enrollment.groupby('Region')['Grade 12 ABM'].sum()
grade_12_HUMSS_per_region = enrollment.groupby('Region')['Grade 12 HUMSS'].sum()
grade_12_STEM_per_region = enrollment.groupby('Region')['Grade 12 STEM'].sum()
grade_12_GAS_per_region = enrollment.groupby('Region')['Grade 12 GAS'].sum()
grade_12_TVL_per_region = enrollment.groupby('Region')['Grade 12 TVL'].sum()
grade_12_sports_per_region = enrollment.groupby('Region')['Grade 12 SPORTS'].sum()
grade_12_AnD_per_region = enrollment.groupby('Region')['Grade 12 A&D'].sum()
grade_12_maritime_per_region = enrollment.groupby('Region')['Grade 12 MARITIME'].sum()

# Combine all the strands into a single DataFrame
strands_per_region_gr12 = pd.DataFrame({
    'ABM': grade_12_ABM_per_region,
    'HUMSS': grade_12_HUMSS_per_region,
    'STEM': grade_12_STEM_per_region,
    'GAS': grade_12_GAS_per_region,
    'TVL': grade_12_TVL_per_region,
    'SPORTS': grade_12_sports_per_region,
    'A&D': grade_12_AnD_per_region,
    'MARITIME': grade_12_maritime_per_region
})

# Find the most popular strand per region
most_popular_strand_per_region_11 = strands_per_region_11.idxmax(axis=1)
most_popular_strand_counts_11 = strands_per_region_11.max(axis=1)
most_popular_strand_per_region_12 = strands_per_region_gr12.idxmax(axis=1)
most_popular_strand_counts_12 = strands_per_region_gr12.max(axis=1)

# Calculate the percentage decrease from Grade 11 to Grade 12 for the most popular strands
percentage_decrease = ((most_popular_strand_counts_11 - most_popular_strand_counts_12) / most_popular_strand_counts_11) * 100


# Combine the results into a single DataFrame
most_popular_strand_summary = pd.DataFrame({
    'Strand 11': most_popular_strand_per_region_11,
    'Count 11': most_popular_strand_counts_11,
    'strand 12': most_popular_strand_per_region_12,
    'Count 12': most_popular_strand_counts_12,
    'percent decrease' : percentage_decrease
})

print("Most popular strand per region with student counts per grade level:")
print(most_popular_strand_summary)




# --------------------survival rate of students per strand--------------------

# Calculate survival rates for each strand
survival_rate_ABM = f'{(enrollment["Grade 12 ABM"].sum() / enrollment["Grade 11 ABM"].sum())*100:.2f}%'
survival_rate_HUMSS = f'{(enrollment["Grade 12 HUMSS"].sum() / enrollment["Grade 11 HUMSS"].sum())*100:.2f}%'
survival_rate_STEM = f'{(enrollment["Grade 12 STEM"].sum() / enrollment["Grade 11 STEM"].sum())*100:.2f}%'
survival_rate_GAS = f'{(enrollment["Grade 12 GAS"].sum() / enrollment["Grade 11 GAS"].sum())*100:.2f}%'
survival_rate_TVL = f'{(enrollment["Grade 12 TVL"].sum() / enrollment["Grade 11 TVL"].sum())*100:.2f}%'
survival_rate_sports = f'{(enrollment["Grade 12 SPORTS"].sum() / enrollment["Grade 11 SPORTS"].sum())*100:.2f}%'
survival_rate_AnD = f'{(enrollment["Grade 12 A&D"].sum() / enrollment["Grade 11 A&D"].sum())*100:.2f}%'
survival_rate_maritime = f'{(enrollment["Grade 12 MARITIME"].sum() / enrollment["Grade 11 MARITIME"].sum())*100:.2f}%'

# Combine survival rates into a single DataFrame
survival_rates = pd.DataFrame({
    'Strand': ['ABM', 'HUMSS', 'STEM', 'GAS', 'TVL', 'SPORTS', 'A&D', 'MARITIME'],
    'Survival Rate': [survival_rate_ABM, survival_rate_HUMSS, survival_rate_STEM, survival_rate_GAS, survival_rate_TVL, survival_rate_sports, survival_rate_AnD, survival_rate_maritime]
}).sort_values(by='Survival Rate', ascending=False)

print("\nSurvival rates of students per strand:")
print(survival_rates)