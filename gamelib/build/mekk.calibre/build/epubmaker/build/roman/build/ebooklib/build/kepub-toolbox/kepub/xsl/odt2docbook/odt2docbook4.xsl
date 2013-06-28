<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<!-- odt2docbook4.xsl version 2.2 -->

<xsl:template match="/">
  <xsl:apply-templates/>
</xsl:template>

<xsl:template match="*">
  <xsl:copy>
    <xsl:apply-templates/>
  </xsl:copy>
</xsl:template>

<xsl:template match="chapter/section">
  <xsl:copy>
    <xsl:apply-templates/>
    <xsl:if test="header2">
      <xsl:text disable-output-escaping="yes"><![CDATA[</section>]]></xsl:text>      
    </xsl:if>
  </xsl:copy>
</xsl:template>


<xsl:template match="chapter/section/header2[position()=1]">
  <xsl:text disable-output-escaping="yes"><![CDATA[<section>]]></xsl:text>
  <title>
    <xsl:value-of select="."/>
  </title>
</xsl:template>

<xsl:template match="chapter/section/header2[not(position()=1)]">
  <xsl:text disable-output-escaping="yes"><![CDATA[</section><section>]]></xsl:text>
  <title>
    <xsl:value-of select="."/>
  </title>
</xsl:template>

<xsl:template match="para">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="header3">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="header4">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="sidebar">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="bridgehead">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="emphasis">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="imagedata">
  <xsl:copy-of select="."/>
</xsl:template>

<xsl:template match="table">
  <xsl:copy-of select="."/>
</xsl:template>

</xsl:stylesheet>
